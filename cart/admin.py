from django.contrib import admin
from .models import OrderItem, Order, ShippingModel
# Register your models here.
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingModel)
