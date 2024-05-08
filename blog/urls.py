from . import views
from core import admin
from django.urls import path




app_name = 'blog'
urlpatterns = [


    path('posts/', views.post_list, name='posts'),
    path('category/<slug>/', views.CategoryAndSubView.as_view(), name='category_sub'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('comments/<int:id>/', views.comment_post, name='comment_post'),
    path('reply/<int:id>/<int:comment_id>/', views.comment_replay, name='comment_replay'),
    # path('by_category/,<int:category_id>/', post_list_by_category, name='post_cat'),
    
     
]