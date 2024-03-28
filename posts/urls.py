from django.urls import path
from posts.views import*

urlpatterns = [
    path('feeds/', feeds),
    path('comment_add/', comment_add),
]