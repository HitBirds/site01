from datetime import datetime
import uuid


from django.db import models


from stdimage.models import StdImageField


# Create your models here.
class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey('Category',on_delete=models.SET_DEFAULT,default=1,related_name='blogs',verbose_name="分类")
    title = models.CharField('标题',max_length=30)
    banner = StdImageField(verbose_name = '文章导航图片',upload_to='blog_banner',
                                  variations={'thumbnail': {'width': 300, 'height': 75}})
    pub_time = models.DateTimeField(False,auto_now_add=True)
    update_time = models.DateTimeField(True,auto_now_add=False,default=datetime.now)
    author = models.ForeignKey('user.Company',on_delete=models.SET_DEFAULT,default=1,related_name='blogs',verbose_name="作者")
    content = models.TextField("文章内容")
    abstract = models.CharField('文章摘要',max_length=140)
    slug = models.SlugField('文章短链接',max_length=100,unique=True)
    views = models.PositiveIntegerField('浏览数',default=0)

    class Meta:
        ordering = ["pub_time"]
        verbose_name = "博客"
        verbose_name_plural=verbose_name

    def __str__(self):
        return '{}'.format(self.title)


class Category(models.Model):
    name = models.CharField('分类',max_length=30,default='未分类')

    class Meta:
        verbose_name = "分类"
        verbose_name_plural=verbose_name

    def __str__(self):
        return '{}'.format(self.name)


class Comment(models.Model):
    username = models.CharField('留言者名',max_length=30)
    head_img = models.ImageField('留言者头像',upload_to='comment_user')
    comment_time = models.DateTimeField('评论时间',False,auto_now_add=True)
    email = models.EmailField(verbose_name='留言者邮箱')
    content = models.TextField(verbose_name='留言内容')
    blog = models.ForeignKey('Blog',on_delete=models.CASCADE,related_name='comments',verbose_name="评论")
    class Meta:
        ordering = ["comment_time"]
        verbose_name = "评论"
        verbose_name_plural=verbose_name