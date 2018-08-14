# -*- coding:utf-8 -*-
__author__ = 'Cliff Huang'
__date__ = '2018/8/12 15:58'

from django import forms
from widgets.markdown import MarkdownWidget

class CommentForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    md_content = forms.CharField(widget=MarkdownWidget)
    blog = forms.SlugField()