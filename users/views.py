from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from users.forms import LoginForm

# Create your views here.

def login_view(request):
    #이미 로그인 되어있다면 
    if request.user.is_authenticated:
        return redirect('/posts/feeds/')
    
    if request.method == 'POST':
    # LoginForm 인스턴스를 만들며, 입력 데이터는 request.POST를 사용
        form = LoginForm(data=request.POST) # 이렇게 data 인수를 채운 채로 생성된 form은 해당 data의 유효성을 검증하기 위해 사용된다.

        #LoginForm에 들어온 데이터가 적절한지 유효성 검사 
        print('form.is_valid():',form.is_valid()) # is_valid 메서드를 실행하기 전에는 cleaned_data에 접근할 수 없음 

        #유효성 검사 이후에는 cleaned_data에서 데이터를 가져와 사용 
        print("form.cleaned_data:", form.cleaned_data)
        context = {"form": form }
        return render(request, 'users/login.html', context)
    else:
    #생성한 LoginForm 인스턴스를 템플릿에 'form'이라는 키로 전달한다.
        form = LoginForm()
        context = {"form": form }
        return render(request, 'users/login.html', context)
