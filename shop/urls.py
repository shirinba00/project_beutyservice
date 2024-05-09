from . import views
from core import admin
from django.urls import path




app_name = 'shop'
urlpatterns = [


    path ('products/', views.AllProducts.as_view() ,name = 'Allproducts'),
    path('category/<slug>/',views.AllProducts.as_view(), name='cat_prod'),
    path('<slug:slug>/', views.DetailProductView.as_view(), name='detail_product'),
    # path('category/<slug>/', views.CategoryAndSubView.as_view(), name='category_sub'),
    # path ('service/personservice/', views.PersonServiceView.as_view() ,name = 'personservice'),
    # path('service/personservice/<int:personservice_id>/', views.personservice_detail, name='detail_personservice'),     
]