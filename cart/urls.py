from django.urls import path
from .views import cart_summary, update_item, checkout, process_order

app_name = 'cart'

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('cart-summary/', cart_summary, name='cart-summary'),
    path('update_item/', update_item, name='update_item'),
    path('process_order/', process_order, name='process_order')

    ]