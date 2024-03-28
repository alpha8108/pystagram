from django.shortcuts import render, redirect

# Create your views here.

def login_view(request):
    #이미 로그인 되어있다면 
    if request.user.is_authenticated:
        return redirect('/posts/feeds/')
    return render(request, 'users/login.html')
