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
        # LoginForm에 전달된 데이터가 유효하다면
        if form.is_valid():
            #username과 password 값을 가져와 변수에 할당
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # username, password에 해당하는 사용자가 있는지 검사
            user = authenticate(username=username, password=password)

            #해당 사용자가 존재한다면 
            if user: 
                #로그인 처리 후, 피드 페이지로 redirect
                login(request, user)
                return redirect('/posts/feeds/')
            # 사용자가 없다면 '실패했습니다' 로그 출력
            else:
                print("로그인에 실패했습니다.")

        #어떤 경우든 실패한 경우(데이터 검증, 사용자 검사) 다시 LoginForm을 사용한 로그인 페이지 렌더링
        context = {"form": form }
        return render(request, 'users/login.html', context)
    else:
    #생성한 LoginForm 인스턴스를 템플릿에 'form'이라는 키로 전달한다.
        form = LoginForm()
        context = {"form": form }
        return render(request, 'users/login.html', context)
