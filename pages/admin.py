from django.contrib import admin
from . import models


@admin.register(models.AboutUS)
class AboutUSAdmin(admin.ModelAdmin):
    list_display = ['title','text_short','information',
                    'cover','file','email','phone',
                    'experience_years','address','customers_number',]


@admin.register(models.ImageAboutUs)
class ImageAboutUsAdmin(admin.ModelAdmin):
    list_display = ['name','image','aboutus',]
                  