from django.contrib import admin
from django.utils.html import format_html

from .models import *


# Register your models here.
@admin.register(Cite)
class CiteAdmin(admin.ModelAdmin):
    list_display = ("header","name","copy_right")


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("img_std","url","update")
    readonly_fields = ("img_std",)
    fields = ("img_std", "img", "url",)

    def img_std(self,obj):
        if obj.img:
            return format_html(
                '<img src="{}" />',obj.img.thumbnail.url
            )
        else:
            return "上传图片"
    img_std.short_description = "图片预览"


@admin.register(ImgGallery)
class ImgGalleryAdmin(admin.ModelAdmin):
    list_display = ("img","url","update")
    readonly_fields = ("img_std",)
    fields = ("img_std", "img", "url",)

    def img_std(self, obj):
        if obj.img:
            return format_html(
                '<img src="{}" />', obj.img.thumbnail.url
            )
        else:
            return "上传图片"

    img_std.short_description = "图片预览"


@admin.register(RelateObjs)
class RelateObjsAdmin(admin.ModelAdmin):
    list_display = ("title","abstract","url")