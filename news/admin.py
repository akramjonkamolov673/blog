from django.contrib import admin
from news.models import PostModel,Comment

# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display=['title','created_at','author']

admin.site.register(PostModel,PostModelAdmin)

class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['content']

admin.site.register(Comment,CommentModelAdmin)