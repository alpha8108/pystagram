from django.db.models import ManyToManyField
from django.forms import CheckboxSelectMultiple
from django.contrib import admin
from posts.models import Post, PostImage, Comment, HashTag
import admin_thumbnails #pip install django-admin-thumbnails 설치한 후에 


# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

#썸네일 라이브러리를 사용
@admin_thumbnails.thumbnail('photo')
class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1
    

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'content',
    ]
    inlines = [
        CommentInline,
        PostImageInline,
    ]
    # Post변경 화면에서 ManyToManyField를 Checkbox로 출력
    formfield_overrides = {
        ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'post',
        'photo',
    ]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'post',
        'content',
    ]

@admin.register(HashTag)
class HashTagAdmin(admin.ModelAdmin):
    pass