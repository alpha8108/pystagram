"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index),
]

urlpatterns += static(
    prefix=settings.MEDIA_URL,   # 이렇게 경로를 연결시키면 django가 처리하여 파일을 돌려주게 되는데 이는 
    document_root=settings.MEDIA_ROOT # 개발단계에서만 쓰여야하는 방식 외부요청에 대한 정적파일을 돌려주는 작업은  
    # 웹서버가 당담하는 것이 더효율적 
)
