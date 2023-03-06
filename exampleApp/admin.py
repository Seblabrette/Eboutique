from django.contrib import admin
# Register your models here.

from .models import *

# admin.site.register(Customer)
admin.site.register(Product)
# admin.site.register(Order)
# admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'email']

admin.site.register(Customer,CustomerAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','date_ordered', 'get_cart_items', 'customer']

admin.site.register(Order, OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'quantity', 'order']
    list_filter = ['order']

admin.site.register(OrderItem, OrderItemAdmin)
