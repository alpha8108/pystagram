from django import forms 
from posts.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [ 'post', 'content'] 
        widgets = { 'content': forms.Textarea(attrs={'placeholder':'댓글 달기...'})}

# Form클래스로 위와같이 정의하여 비슷한 데이터를 받으려면
# class CommentForm(forms.Form):
#       content = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '댓글 달기...'})) 
#이런식으로 정의해야한다. 
        
