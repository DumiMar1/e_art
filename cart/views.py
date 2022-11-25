from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
import json
from post.models import Post
from .models import Order, OrderItem, ShippingModel
from django.contrib import messages
from django.http import JsonResponse
import datetime
from .utils import  cart_data, cookie_cart, guest_order

# Create your views here.


def cart_summary(request):

    data = cart_data(request)
    cart_items = data['cartItems']
    items = data['items']
    order = data['order']

    context = {'items': items, 'order': order, 'cartItems': cart_items}
    return render(request, 'cart/cart_view.html', context)


def checkout(request):

    data = cart_data(request)
    cart_items = data['cartItems']
    items = data['items']
    order = data['order']

    context = {'items': items, 'order': order, 'cartItems': cart_items}
    return render(request, 'cart/checkout_view.html', context)


def update_item(request):
    data = json.loads(request.body)
    post_id = data['postId']
    action = data['action']

    user = request.user
    post = Post.objects.get(id=post_id)
    order, created = Order.objects.get_or_create(user=user, complete=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=post)

    if action == 'add':
        order_item.quantity = (order_item.quantity + 1)
    elif action == 'remove':
        order_item.quantity = (order_item.quantity - 1)
 
    
    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()
    return JsonResponse('Item was added', safe=False)


def process_order(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)

    else:
        user, order = guest_order(request, data)
        

    total = float(data['form']['total'])
    order.transaction_id = transaction_id
    if total == order.get_cart_total:
        order.complete = True
    order.save()

    ShippingModel.objects.create(
            user = user,
            order = order,
            address = data['shipping']['address'],
            city = data['shipping']['city'],
            zipcode = data['shipping']['zipcode'],
        )

        
    return JsonResponse('Payment complete!', safe=False)








