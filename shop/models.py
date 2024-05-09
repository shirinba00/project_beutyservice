from django.db import models
from django.urls import reverse
from django.conf import settings
from core.models import CustomUser
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from uuid import uuid4
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from django.db.models import Avg

class CategoryProduct(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='sub')
    sub_cat = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(allow_unicode=True, unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='category/', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:cat_prod', args=[self.slug, self.id])

class Product(models.Model):
    slug = models.SlugField(allow_unicode=True, unique=True, null=True, blank=True,)
    name = models.CharField(max_length=200,)
    information_short = RichTextUploadingField(blank=True, null=True,)
    unit_price = models.IntegerField()
    discount = models.IntegerField(blank=True, null=True,)
    total_price = models.IntegerField()
    count = models.PositiveIntegerField()
    available = models.BooleanField(default=True,)
    created_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)
    expire_date = models.CharField(max_length=50, blank=True, null=True,)
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, related_name='product_brands', null=True, blank=True,)
    company = models.ForeignKey('Company', on_delete=models.PROTECT, related_name='product_company', blank=True, null=True,)
    country = models.ForeignKey('Country', on_delete=models.PROTECT, blank=True, null=True,related_name='product_country')
    category = models.ManyToManyField(CategoryProduct, blank=True, related_name='product_category')
    SKU = models.CharField(max_length=200, blank=True, null=True,)
    image = models.ImageField(upload_to='product/',)
    favourite = models.ManyToManyField(CustomUser, blank=True, related_name='fa_user',)
    total_favourite = models.IntegerField(default=0,)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.discount:
            self.total_price = self.unit_price
        elif self.discount:
            total = (self.discount * self.unit_price) / 100
            self.total_price = int(self.unit_price - total)
        super().save(*args, **kwargs)

    # def average(self):
    #     data = Comment.objects.filter(is_replay=False, product=self).aggregate(avg=Avg('star'))
    #     rate = 0
    #     if data['avg'] is not None:
    #         rate = round(data['avg'], )
    #     return rate
    def get_absolute_url(self):
        return reverse('products:single_product', args=[self.slug, self.id])

class Brand(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(allow_unicode=True, unique=True, null=True, blank=True,)

    image = models.ImageField(upload_to='brand/', blank=True, null=True)
    descriptions = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



