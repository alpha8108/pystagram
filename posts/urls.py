from django.urls import path
from posts.views import*

urlpatterns = [
    path('feeds/', feeds),
]