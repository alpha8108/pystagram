from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from users.forms import LoginForm, SignupForm
from users.models import User

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
                login(request, user) # 로그인 함수는 브라우저에 해당 사용자를 유지시켜주는 기능이다. 
                # authenticate가 단순히 폼에 입력한 값이 있는지 검사하고 객체를 돌려준다면 login함수는 로그인했다면 로그인 상태로 변환 및 유지 기능을 담당 로그인 함수 호출에는 현재요청(request)객체와 사용자(User)객체가 필요하다
                return redirect('/posts/feeds/')
            # 사용자가 없다면 form에 에러 추가
            else:
                form.add_error(None, "입력한 자격증명에 해당하는 사용자가 없습니다.") # 특정필드에 국한된 문제가 아니라면 None으로 지정

        #어떤 경우든 실패한 경우(데이터 검증, 사용자 검사) 다시 LoginForm을 사용한 로그인 페이지 렌더링
        context = {"form": form }
        return render(request, 'users/login.html', context)
    else:
    #생성한 LoginForm 인스턴스를 템플릿에 'form'이라는 키로 전달한다.
        form = LoginForm()
        context = {"form": form }
        return render(request, 'users/login.html', context)

def logout_view(request):
    # logout 함수 호출에 request를 전달한다
    logout(request)
    # logout 처리 후, 로그인 페이지로 이동한다
    return redirect('/users/login')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            profile_image = form.cleaned_data['profile_image']
            short_description = form.cleaned_data['short_description']
            
            # 비밀번호와 비밀번호 확인의 값이 같은 지 검사 
            if password1 != password2:
                form.add_error('password2', '비밀번호와 비밀번호 확인란의 값이 다릅니다.')

            # username을 사용 중인 User가 이미 있는 지 검사
            if User.objects.filter(username=username).exists():
                form.add_error("username", "입력한 사용자명은 이미 사용중입니다.")
            
            #에러가 존재한다면, 에러를 포함한 form을 사용해 회원가입 페이지를 다시 렌더링 
            if form.errors:
                context = {'form': form }
                return render(request, 'users/signup.html', context)
            #에러가 없다면, 사용자를 생성하고 로그인 처리 후 피드 페이지로 이동 
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password1,
                    profile_image=profile_image,
                    short_description=short_description,
                )
                login(request, user)
                return redirect('/posts/feeds/')
            
    #GET 요청에서는 빈 Form을 보여준다.
    else:
        form = SignupForm()
        context = {'form': form }
        return render(request, 'users/signup.html', context)