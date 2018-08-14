from django.shortcuts import render
from django.db.models import Count
from django.core.paginator import Paginator
from django.views.generic.base import View
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.http import HttpResponse


from site01.settings import EMAIL_FROM

from plugins.models import *
from .models import *
from blog.models import *
from .forms import EmailForm
# Create your views here.

def get_base():
    cite = {}
    try:
        cite = Cite.objects.latest('id')
    except Cite.DoesNotExist:
        cite['name'] = 'ukn'
        cite['header'] = 'ukn'
        cite['copy_right'] = 'ukn'

    banner_list = []
    try:
        banner_list = Banner.objects.order_by('-update')[0:3]
    except IndexError:
        pass
    if not banner_list.exists():
        banner_list = []
        for i in range(3):
            banner_list.append({'img':{'url':"/static/images/slide1.jpg"},'url':'#'})

    image_list = []
    try:
        image_list = ImgGallery.objects.order_by('-update')[0:6]
    except IndexError:
        pass
    if not image_list.exists():
        image_list = []
        for i in range(6):
            image_list.append({'img':{'url':"/static/images/gal1.jpg"},'url':'#'})

    category_dict = {}
    try:
        categories = Category.objects.all()
        for category in categories:
            category_dict[category.name] = category.blogs.values('title','slug')
    except Category.DoesNotExist:
        pass

    company = Company.objects.first()

    try:
        company.services = company.service.values('name', 'url')
    except:
        pass

    context = {'cite':cite,'banner_list':banner_list,'image_list':image_list,'company':company,'category_dict':category_dict}
    return context


def index(request):
    context = get_base()
    try:
        articles = Blog.objects.values('title','pub_time','author__name','category__name','banner','abstract','slug',n_comments=Count('comments'))
        paginator = Paginator(articles,3)
        page = request.GET.get('page',1)
        contacts = paginator.get_page(page)
        context['contacts'] = contacts
    except:
        pass
    return render(request,'index.html',context=context)

def support_view(request):
    context = get_base()
    return render(request,'support.html',context=context)


def about_view(requset):
    context = get_base()
    return render(requset,'about.html',context=context)


class ContactView(View):
    def get(self,request):
        context = get_base()
        return render(request, 'contact.html', context=context)

    def post(self,request):
        email_form = EmailForm(request.POST)
        if email_form.is_valid():
            name = email_form.cleaned_data['name']
            email = email_form.cleaned_data['email']
            message = email_form.cleaned_data['message']

            email_title = "geekcug User Send"
            email_body = 'name:{}\nemail:{}\ncontent:{}'.format(name,email,message)
            email_to = "hcg19113225@gmail.com"
            send_status = send_mail(email_title,email_body,EMAIL_FROM,[email_to])
            if send_status:
                return HttpResponse('发送成功')
            else:
                return HttpResponse('发送失败')
        else:
            return HttpResponse('邮件格式验证失败')