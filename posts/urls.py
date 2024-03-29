from django.urls import path
from posts.views import*

app_name= 'posts'

urlpatterns = [
    path('feeds/', feeds, name='feeds'),
    path('comment_add/', comment_add, name='comment_add'),
    path('comment_delete/<int:comment_id>/', comment_delete, name='comment_delete'),
    path('post_add/', post_add, name='post_add'),
]