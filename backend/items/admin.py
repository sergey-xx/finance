from django.contrib import admin

from .models import Item, Order, Coupon


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'item', 'quantity')


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'name', 'coupon_id')
