from django.contrib import admin
from .models import Company,Service
# Register your models here.


class MyAdminSite(admin.AdminSite):
    site_header = '公司2333'
    index_title = 'hahahaha'
    site_title = '2333'


class CompanyAdmin(admin.ModelAdmin):
    filter_horizontal = ['service']
    empty_value_display = '-empty-'


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name']
    empty_value_display = '-empty-'


admin_site = MyAdminSite(name='myadmin')
admin_site.register(Company,CompanyAdmin)
admin_site.register(Service,ServiceAdmin)
