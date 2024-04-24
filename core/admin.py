from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import CustomUser
from core import models


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['email','username',]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username","email", "password1", "password2","first_name","last_name")
                          
            },
        ),
    )







admin.site.register(models.OTPRequest)