from . import views
from core import admin
from django.urls import path




app_name = 'blog'
urlpatterns = [


    path('posts/', views.post_list, name='posts'),
    path('category/<slug>/<int:id>/', views.category_and_sub, name='cat'),
    # path('<slug:slug>/', post_detail, name='post_detail'),
    # path('by_category/,<int:category_id>/', post_list_by_category, name='post_cat'),
    # path('comments/<int:id>/', comment_post, name='comment_create'),
    
     
]