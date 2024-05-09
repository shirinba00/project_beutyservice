from . import views
from core import admin
from django.urls import path




app_name = 'shop'
urlpatterns = [


    path ('shop/', views.AllTypeServiceView.as_view() ,name = 'Allproducts'),
    # path('<slug:slug>/', views.DetailTypeServiceView.as_view(), name='detail_service'),
    # path('category/<slug>/', views.CategoryAndSubView.as_view(), name='category_sub'),
    # path ('service/personservice/', views.PersonServiceView.as_view() ,name = 'personservice'),
    # path('service/personservice/<int:personservice_id>/', views.personservice_detail, name='detail_personservice'),     
]