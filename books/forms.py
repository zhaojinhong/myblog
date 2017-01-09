# -*- coding: utf-8 -*-
# @Author: zhaojinhong
# @Date:   2016-12-30 10:35:13
# @Last Modified by:   zhaojinhong
# @Last Modified time: 2017-01-06 18:31:37
from django import forms
class RegistForm(forms.Form):
	username = forms.CharField(min_length=3, max_length=20)
	password = forms.CharField(min_length=3, max_length=20)
	email = forms.EmailField(min_length=3, max_length=20)
	repassword = forms.CharField(min_length=3,max_length=20)
	avatar = forms.FileField(max_length=100)    



