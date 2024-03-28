from django.shortcuts import render, redirect 
from posts.models import Post

# Create your views here.

def feeds(request):
    #요청에 포함된 사용자가 로그인하지 않은 경우(AnonymousUser인 경우)
    if not request.user.is_authenticated:
        return redirect('/users/login/')
    
    # 모든 글 목록을 템플릿으로 전달 
    posts = Post.objects.all()
    context = {'posts': posts }
    return render(request, 'posts/feeds.html', context)
