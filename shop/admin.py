from django.contrib import admin
# from . import models

# class CartItemInline(admin.TabularInline):
#     model = models.CartItem
#     fields = ['typeservice','quantity','id',]
#     extra= 0 
#     min_num = 1



# @admin.register(models.Cart)
# class CartAdmin(admin.ModelAdmin):
#     list_display = ['id','created_at',]
#     inlines = [CartItemInline]

# class OrderItemInline(admin.TabularInline):
#     model = models.OrderItem
#     fields = ['typeservice','quantity','unit_price',]
#     extra= 0 
#     min_num = 1

# @admin.register(models.Order)
# class OrderAdmin(admin.ModelAdmin):
#     model = models.Order
#     list_display = ['id','status','datetime_created',]
#     inlines = [OrderItemInline]





