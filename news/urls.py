from django.urls import path
from news.views import home,post_detail,post_edit,post_delete

urlpatterns = [
    path('',home,name='home-page'),
    path('post_detail/<int:pk>',post_detail,name='post_detail-page'),
    path('post_edit/<int:pk>',post_edit,name='post_edit-page'),
    path('post_delete/<int:pk>,',post_delete,name='post_delete-page')
]
