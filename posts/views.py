from django.shortcuts import render, redirect 

# Create your views here.

def feeds(request):
    #요청에 포함된 사용자가 로그인하지 않은 경우(AnonymousUser인 경우)
    if not request.user.is_authenticated:
        # /users/login/ URL로 이동시킴
        return redirect('/users/login/')
    return render(request, 'posts/feeds.html')
