from django.contrib import admin
from .models import Product, Cart, Vegetable, Dal_Rice
from .models import Cookies_Snakes, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ('P_name', 'P_price', 'P_stock')


class CartAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'item')


class VegetableAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class Dal_RiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class Cookies_SnakesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'item', 'bill_amount', 'date')


admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Vegetable, VegetableAdmin)
admin.site.register(Dal_Rice, Dal_RiceAdmin)
admin.site.register(Cookies_Snakes, Cookies_SnakesAdmin)
admin.site.register(Order, OrderAdmin)