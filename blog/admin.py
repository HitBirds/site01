from django.db import models
from django.contrib import admin
from django.utils.html import format_html

from .models import Blog,Comment,Category

from widgets.markdown import MarkdownWidget

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_time'
    empty_value_display = '-empty-'
    fields = ('title','author','category','abstract',"img_std",'banner','content','slug')
    formfield_overrides = {models.TextField:{'widget':MarkdownWidget}}
    radio_fields = {'category':admin.HORIZONTAL}
    readonly_fields = ['pub_time','update_time','id','img_std']
    ordering = ['pub_time']
    search_fields = ['content']
    prepopulated_fields = {'slug':("title",)}

    list_display = ['title','author','category','abstract']

    def img_std(self, obj):
        if obj.img:
            return format_html(
                '<img src="{}" />', obj.img.thumbnail.url
            )
        else:
            return "上传图片"

    img_std.short_description = "图片预览"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fieldsets = (
        (None,{
            'fields':(('head_img','username'),'content','blog')
        }),
        ('Advanced options',{
            'classes':('collapse',),
            'fields':('email',),
        }),
    )
    empty_value_display = '-empty-'
    autocomplete_fields = ['blog']
