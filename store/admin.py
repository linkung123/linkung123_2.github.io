from django.contrib import admin

# Register your models here.
from .models import Product, Cart, CartItem, Order, OrderItem

admin.site.register(Product)
class CartItemInline(admin.TabularInline):
    model = CartItem

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]

class OrderItemInline(admin.TabularInline):
    model = OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]

# admin.sites.register(Product): 註冊 Product 模型, 以便在 Django 管理後台中管理商品
# CartItemInline 類: 創建一個內聯類, 用於在 Cart 管理頁面中直接編輯 CartItem
# CartAdmin 類: 註冊 Cart 模型, 指定 CartItemInline 作為內聯, 這樣在 Cart 管理頁面中就可以直接編輯 CartItem
# OrderItemInline 類: 創建一個內聯類, 用於在 Order 管理頁面中直接編輯 OrderItem
# OrderAdmin 類: 註冊 Order 模型, 指定 OrderItemInline 作為內聯, 這樣在 Order 管理頁面中就可以直接編輯 OrderItem