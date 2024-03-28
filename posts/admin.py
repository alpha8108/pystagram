from django.contrib.admin.widgets import AdminFileWidget
from django.db import models
from django.utils.safestring import mark_safe
from django.contrib import admin
from posts.models import Post, PostImage, Comment

# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

# AdminFileWidget은 관리자 페이지에서 '파일 선택' 버튼을 보여주는 부분이다.
# 이 Widget을 커스텀하여, <img> 태그를 추가한다 
class InlineImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        html = super().render(name, value, attrs, renderer)
        if value and getattr(value, 'url', None):
            html = mark_safe(f'<img src="{value.url}" height=150>') + html
        return html


class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1
    formfield_overrides = {
        models.ImageField: {
            "widget": InlineImageWidget,
        }
    }

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
