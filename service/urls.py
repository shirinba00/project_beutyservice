from . import views
from core import admin
from django.urls import path




app_name = 'service'
urlpatterns = [


    path ('service/', views.AllTypeServiceView.as_view() ,name = 'typeservice'),
    path('<slug:slug>/', views.DetailTypeServiceView.as_view(), name='detail_service'),
    path('category/<slug>/', views.CategoryAndSubView.as_view(), name='category_sub'),


  
]