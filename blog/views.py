from django.views.generic.base import View
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.db.models import Q
from django.db.models import Count

from user.views import get_base
from .forms import CommentForm
from .models import *
# Create your views here.
class BlogView(View):
    def get(self,request,blog_slug=None):
        context = get_base()
        article = None
        if blog_slug is not None:
            try:
                article = Blog.objects.filter(slug=blog_slug).first()
                article.views+=1
                article.save()
                article.n_comments = article.comments.count()
                article.comment_list = article.comments.values('username', 'head_img', 'comment_time', 'content')
            except:
                pass
        else:
            try:
                article = Blog.objects.last()
                article.n_comments = article.comments.count()
                article.comment_list = article.comments.values('username', 'head_img', 'comment_time', 'content')
            except:
                pass
        context['article'] = article
        return render(request, 'blog.html', context=context)

    def post(self,request):
        comment = CommentForm(request.POST)
        if comment.is_valid():
            name = comment.cleaned_data['name']
            email = comment.cleaned_data['email']
            md_content = comment.cleaned_data['md_content']
            blog = comment.cleaned_data['blog']
            head_img = 'comment_user/userpic.gif'
            Comment(username=name,email=email,head_img=head_img,content=md_content,blog=Blog.objects.get(slug=blog)).save()
            return redirect('blog',blog_slug=blog)
        else:
            return HttpResponse('表单验证失败')

class SearchView(View):
    def get(self,request):
        return redirect('index')
    def post(self,request):
        articles = []
        keywords = request.POST.get('editbox_search','')
        try:
            articles = Blog.objects.filter(Q(title__icontains=keywords)|Q(abstract__icontains=keywords)|Q(content__icontains=keywords)).values('title','pub_time','author__name','category__name','banner','abstract','slug',n_comments=Count('comments'))
        except:
            articles = [{'abstract':'未找到匹配的结果'}]
        context = get_base()
        context['contacts'] = articles
        return render(request,'index.html',context=context)