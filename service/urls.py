from . import views
from core import admin
from django.urls import path




app_name = 'service'
urlpatterns = [


    path ('service/', views.all_typeservice ,name = 'typeservice'),

  
]