from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=30,verbose_name='公司名',default='未知')
    address = models.CharField(max_length=30,verbose_name='公司地址')
    telephone = models.CharField('电话号',max_length=30)
    email = models.EmailField(verbose_name='电子邮箱')
    git = models.URLField(verbose_name='URL地址')
    mission = models.TextField(verbose_name='职责')
    about = models.TextField(verbose_name='关于我们')
    support = models.TextField(verbose_name='服务简介')
    service = models.ManyToManyField('Service',related_name='companies_of',verbose_name="服务项")
    qq = models.CharField(verbose_name='QQ号',max_length=20)

    class Meta:
        verbose_name = "公司信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}-{}'.format(self.name,self.telephone)

class Service(models.Model):
    name = models.CharField('服务项',max_length=30)
    url = models.URLField(verbose_name='URL示例地址')

    class Meta:
        verbose_name = "公司服务"
        verbose_name_plural = verbose_name