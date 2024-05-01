from . import views
from core import admin
from django.urls import path


app_name = 'pages'
urlpatterns = [

    path ('aboutus/', views.AllAboutUsView.as_view() ,name = 'aboutus'),
    path ('contactus/', views.ContactUsView.as_view() ,name = 'contactus'),
]