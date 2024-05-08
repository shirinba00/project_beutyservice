from django.contrib import admin

from .models import  Comment, Post,Category




@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ['title', 'title_english', 'status', 'datetime_modified','datetime_created',]
    ordering = ('status',)
    prepopulated_fields = {
        'slug': ('title_english',)
    }


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'datetime_update')
    list_filter = ['name', ]
    prepopulated_fields = {

        'slug': ('name',)
    }



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('fullname','email','text', 'datetime_created','is_reply','replay_id')