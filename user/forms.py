# -*- coding:utf-8 -*-
__author__ = 'Cliff Huang'
__date__ = '2018/8/14 15:05'

from django import forms
class EmailForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()