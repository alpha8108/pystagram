
from django.db import models

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey('users.User', verbose_name='작성자', on_delete=models.CASCADE)
    content = models.TextField('내용')
    created = models.DateTimeField('생성일시', auto_now_add=True)
    tags = models.ManyToManyField('posts.HashTag', verbose_name='해시태그 목록', blank=True)
    # '앱이름.모델클래스이름' 형태로 문자열을 지정하면 아래쪽에 선언한 Model클래스도 참조할 수 있음
    
    def __str__(self):
        return f"{self.user.username}의 Post(id: {self.id})"
    

class PostImage(models.Model):
    post = models.ForeignKey(Post, verbose_name='포스트', on_delete=models.CASCADE)
    photo = models.ImageField('사진', upload_to='post')

class Comment(models.Model):
    user = models.ForeignKey("users.User", verbose_name='작성자', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name='포스트', on_delete=models.CASCADE)
    content = models.TextField("내용")
    created = models.DateTimeField('생성일시', auto_now_add=True)

class HashTag(models.Model):
    name = models.CharField("태그명", max_length=50)

    def __str__(self):
        return self.name