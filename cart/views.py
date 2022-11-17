from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
import json
from post.models import Post
from .models import Order, OrderItem
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.


def cart_summary(request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items

    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cart_items = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems': cart_items}
    return render(request, 'cart/cart_view.html', context)


def checkout(request):
    if request.user.is_authenticated:
        # data = json.loads(request.body)
        # value = data['itemValue']
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cart_items = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems': cart_items}
    return render(request, 'cart/checkout_view.html', context)


def update_item(request):
    data = json.loads(request.body)
    post_id = data['postId']
    action = data['action']
    # value = data['itemValue']
    user = request.user
    post = Post.objects.get(id=post_id)
    order, created = Order.objects.get_or_create(user=user, complete=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=post)

    if action == 'add':
        order_item.quantity = (order_item.quantity + 1)
    elif action == 'remove':
        order_item.quantity = (order_item.quantity - 1)
    # elif action == 'modify':
    #     order_item.item_type = value
    
    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()
    return JsonResponse('Item was added', safe=False)


def process_order(request):
    print('Data:', request.body)
    return JsonResponse('Payment complete!', safe=False)








