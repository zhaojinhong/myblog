# -*- coding: utf-8 -*-
# @Author: zhaojinhong
# @Date:   2016-12-30 10:35:13
# @Last Modified by:   zhaojinhong
# @Last Modified time: 2017-01-09 15:34:46
from django import forms
class RegistForm(forms.Form):
	username = forms.CharField(min_length=3, max_length=20,error_messages={'min_length':u'用户名不能少于3位'})
	password = forms.CharField(max_length=20)
	email = forms.EmailField(min_length=3, max_length=20)
	repassword = forms.CharField(min_length=3,max_length=20)
	avatar = forms.FileField(max_length=100)    


	def clean_password(self):   #验证密码，密码长度小于3位，抛出异常
		password = self.cleaned_data.get('password',None)
		if len(password) < 3:
			#raise forms.ValidationError(u'密码不能小于3位',code=u'密码无效')
			self.add_error('password','password error')


	def clean(self):   #全局
		pass