from django.db import models

from stdimage.models import StdImageField


# Create your models here.
class Cite(models.Model):
    header = models.CharField('logo',max_length=30)
    name = models.CharField('站名',max_length=30)
    copy_right = models.CharField('版权',max_length=40)

    class Meta:
        verbose_name = "站点信息"
        verbose_name_plural=verbose_name


class Banner(models.Model):
    img = StdImageField(verbose_name = '图片',upload_to='banner',
                                  variations={'thumbnail': {'width': 200, 'height': 75}})
    update = models.DateTimeField('上传时间',False,auto_now_add=True)
    url = models.URLField(verbose_name='图片指向链接')

    class Meta:
        verbose_name = "站点导航图"
        verbose_name_plural=verbose_name


class ImgGallery(models.Model):
    img = StdImageField(verbose_name = '图片',upload_to='gallery',
                               variations={'thumbnail': {'width': 75, 'height': 75}})
    update = models.DateTimeField('上传时间',False,auto_now_add=True)
    url = models.URLField(verbose_name="图片指向链接")

    class Meta:
        verbose_name = "图集"
        verbose_name_plural=verbose_name


class RelateObjs(models.Model):
    title = models.CharField('推荐项',max_length=30)
    abstract = models.CharField('推荐摘要',max_length=140)
    url = models.URLField(verbose_name='推荐URL')

    class Meta:
        verbose_name = "推荐管理"
        verbose_name_plural=verbose_name