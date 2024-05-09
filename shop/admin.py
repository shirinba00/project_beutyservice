from django.contrib import admin
from . import models



@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    class ProductAdmin(admin.ModelAdmin):
        list_display = ['name', 'slug', 'id', 'count', 'available', 'unit_price', 'discount',
                    'image', 'SKU', 'information_short', 'expire_date', 'favourite']
    list_filter = ('available',)
    # list_editable = ('available', 'unit_price',)
    # search_fields = ('name','category',)
    prepopulated_fields = {
        'slug': ('name',)
    }
    # autocomplete_fields = ['category', ]


@admin.register(models.CategoryProduct)
class CategoryProductsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ['name', ]
    prepopulated_fields = {

        'slug': ('name',)
    }




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





