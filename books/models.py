# -*- coding: utf-8 -*-
# @Author: zhaojinhong
# @Date:   2016-12-13 16:28:11
# @Last Modified by:   zhaojinhong
# @Last Modified time: 2017-01-06 18:31:43
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class BlogModel(models.Model):
	id = models.AutoField(primary_key=True)     #AutoField：自增长类型
	title = models.CharField(max_length=100)    #字符串类型，最大长度100
	content = models.TextField(null=False)		#不指定长度，长度无限制,不能为空
	desc = models.CharField(max_length=100,null=True)

class UserModel(models.Model):
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	email = models.EmailField(max_length=100,null=True)
	repassword = models.CharField(max_length=100,null=True)
	avatar = models.FileField(max_length=100,upload_to='',null=True)     #upload_to  用来保存文件上传的路径  路径需要在setting中设置MEDIA_ROOT=