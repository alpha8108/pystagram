from django import forms
from django.core.exceptions import ValidationError
from users.models import User 
# docs.django.ac/forms/validation  Form에서 각 필드 값의 유효성을 검증하는 방법과 순서를 자세히 설명한 문서 

class LoginForm(forms.Form):
    username = forms.CharField(min_length=3, widget=forms.TextInput(attrs={'placeholder': '사용자명(3자리 이상)'},))
    password = forms.CharField(min_length=4, widget=forms.PasswordInput(attrs={'placeholder': '비밀번호 (4자리 이상)'},))

class SignupForm(forms.Form):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    profile_image = forms.ImageField()
    short_description = forms.CharField()

#p.228페이지 하단 16.6.4 설명 참조 
    def clean_username(self):
        username =  self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError(f'입력한 사용자명({username})은 이미 사용 중입니다.')
        return username
    
    def clean(self): #clean 메서드는 마지막에 값을 리턴하지 않아도 된다.
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            self.add_error('password2', '비밀번호와 비밀번호 확인란의 값이 다릅니다.')

#회원가입과 관련된 모든 데이터가 SignupForm에 존재하므로 
#해당 폼이 회원가입 기능까지 담당해도 괜찮을 것 같다고 해서 코드 리팩터링
    def save(self):
        username = self.cleaned_data['username']
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        profile_image = self.cleaned_data['profile_image']
        short_description = self.cleaned_data['short_description']
        user = User.objects.create_user(
            username=username,
            password=password1,
            profile_image=profile_image,
            short_description=short_description,
        )
        return user
    
# Form은 사용자가 요청에 전달한 데이터들을 검증하고 가공하는데 특화된 기능이다.
# view함수가 지나치게 방대해지는 것을 막는 효과도 있으니,
# 사용자가 전달한 데이터를 처리할 떄는 Form을 사용하도록 하자. 
        