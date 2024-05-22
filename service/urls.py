from . import views
from core import admin
from django.urls import path




app_name = 'service'
urlpatterns = [


    path ('service/', views.AllTypeServiceView.as_view() ,name = 'typeservice'),
    path('<slug:slug>/', views.DetailTypeServiceView.as_view(), name='detail_service'),
    path('category/<slug>/', views.CategoryAndSubView.as_view(), name='category_sub'),
    path ('service/personservice/', views.PersonServiceView.as_view() ,name = 'personservice'),
    path('service/personservice/<int:personservice_id>/', views.personservice_detail, name='detail_personservice'), 
    path('service_by_tag/<int:tag_id>/<slug:slug>/', views.typeservice_list_by_tag, name='service_tag')
    ]