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
        