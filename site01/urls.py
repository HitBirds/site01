"""site01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
import user.views as UserViews
import blog.views as BlogViews
import widgets.views as WidgetViews

from user.admin import admin_site
urlpatterns = [
    path('admin/', admin.site.urls),
    path('myadmin/',admin_site.urls),
    path('',UserViews.index,name='index'),
    path('support/',UserViews.support_view,name='support'),
    path('about/',UserViews.about_view,name='about'),
    path('contact/',UserViews.ContactView.as_view(),name='contact'),
    path('search/',BlogViews.SearchView.as_view(),name='search'),
    path('blog/',BlogViews.BlogView.as_view(),name='blog'),
    path('blog/<slug:blog_slug>/',BlogViews.BlogView.as_view(),name='blog'),
    path('markdown/uploadimage/',WidgetViews.img_upload_view,name = 'md_upload'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [path('__debug__',include(debug_toolbar.urls))] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)