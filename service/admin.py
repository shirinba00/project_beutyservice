from django.contrib import admin
from . import models


@admin.register(models.TypeService)
class TypeServiceAdmin(admin.ModelAdmin):
    list_display = ['status','name','slug', 'info','picture',
                    'category','datetime_created','description','icon']

    list_filter = ('status',)
    search_fields = ('name',)
    prepopulated_fields = {
        'slug': ('name',)
    }

@admin.register(models.SampleGalleryPersonService)
class SampleGalleryPersonServiceAdmin(admin.ModelAdmin):
     list_display = ['name','description','image',]
    # list_filter = ['name']
    # search_fields = ('name',)




class SampleGalleryInline(admin.TabularInline):
    model = models.SampleGalleryPersonService
    fields = ['name','description','image',]
    extra= 0 
    min_num = 1


@admin.register(models.PersonService)
class PersonServiceAdmin(admin.ModelAdmin):
    list_display =  ['first_name','last_name','email']
    ordering = ('user__last_name','user__first_name',)
    search_fields = ('user__email__istartswith','user__last_name__istartswith','user__first_name__istartswith',)
    def first_name(self,personservice):
        return personservice.user.first_name
    
    def last_name(self,personservice):
        return personservice.user.last_name
    
    def email(self,personservice):
        return personservice.user.email





@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display =  ['id','first_name','last_name','email',]
    ordering = ('user__last_name','user__first_name',)
    search_fields = ('user__first_name__istartswith','user__last_name__istartswith',)

    @property
    def first_name(self):
        return self.user.first_name
    
    def last_name(self,customer):
        return customer.user.last_name
    
    def email(self,customer):
        return customer.user.email



@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['city','province','postalcode','street']



@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','sub_category', 'sub_cat', 'id']
    list_filter = ['name']
    prepopulated_fields = {
        'slug': ('name',)
    }
    search_fields = ('name',)

    
@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','text','id','status',]
    list_filter = ['datetime_created','name']
    search_fields = ('name',)




class CartItemInline(admin.TabularInline):
    model = models.CartItem
    fields = ['typeservice','quantity','id',]
    extra= 0 
    min_num = 1



@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id','created_at',]
    inlines = [CartItemInline]

class OrderItemInline(admin.TabularInline):
    model = models.OrderItem
    fields = ['typeservice','quantity','unit_price',]
    extra= 0 
    min_num = 1

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    model = models.Order
    list_display = ['id','status','datetime_created',]
    inlines = [OrderItemInline]




