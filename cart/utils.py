import json
from .models import *

def cookie_cart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    print('cart:', cart)
    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0}
    cart_items = order['get_cart_items']

    for i in cart:
        try:
            cart_items += cart[i]['quantity']
            post = Post.objects.get(id=i)
            total = (post.price * cart[i]['quantity'])

            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']

            item = {
                    'product':{
                        'id':post.id,
                        'title':post.title,
                        'price':post.price,
                        'image':{
                            'url':post.image.url},
                        },
                    'quantity':cart[i]['quantity'],
                    'get_total':total
                }
            items.append(item)
            
        except:
            pass
    
    return {'items': items, 'order': order, 'cartItems': cart_items}


def cart_data(request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items

    else:
        cookie_data = cookie_cart(request)
        cart_items = cookie_data['cartItems']
        items = cookie_data['items']
        order = cookie_data['order']
    return {'items': items, 'order': order, 'cartItems': cart_items}

def guest_order(request, data):
    print('User is not logged in.')
    print('cookies', request.COOKIES)
    name = data['form']['name']
    email = data['form']['email']

    cookie_data = cookie_cart(request)
    items = cookie_data['items']
    user, created = User.objects.get_or_create(
        email=email,
    )
    user.username = name
    user.save()

    order = Order.objects.create(user=user, 
                                complete=False)
    
    for item in items:
        product = Post.objects.get(id=item['product']['id'])

        order_item = OrderItem.objects.create(
            product=product,
            order=order,
            quantity=item['quantity'])
    return user, order