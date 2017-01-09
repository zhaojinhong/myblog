# -*- coding: utf-8 -*-
# @Author: zhaojinhong
# @Date:   2016-12-14 10:25:36
# @Last Modified by:   zhaojinhong
# @Last Modified time: 2017-01-06 18:33:20
from django.shortcuts import render,reverse   ##导入reverse
from django.http import HttpResponse,HttpResponseRedirect
from models import BlogModel,UserModel
import uuid
from forms import RegistForm
# def index(request):
#      #根据url命名的books_article，当访问index时跳转到article；
#      return HttpResponseRedirect(reverse('books_article'))
# def article(request):
#      return HttpResponse('article')
# def index(request):
#     return render(request, 'books.html')
# def article(request,article_id):
#     html = u"页面 %s" % article_id
#     return HttpResponse(html)
def index(request):
	# blogModel = BlogModel(
 #        title = u"这是第一个",
 #        content = u"第一个",
 #        desc = "None"
	# 	)
	# blogModel.save()

	# blogModel = BlogModel.objects.get(id=10)
	# return render(request, 'books.html' , {'blog':blogModel})
    return HttpResponse(u"这是首页")
def delete_books(request):
    #首先找到要删除的数据，
    # blogModel = BlogModel.objects.get(id=1)

    # #然后在删除
    # blogModel.delete()
    # return HttpResponse("delete seccess")
    pass

def login(request):
	# 增加一条用户数据
	# userModel = UserModel(username='zhao',password='111')
	# userModel.save()
	# return HttpResponse('secuss')
	if request.method == 'GET':
		return render(request,'base.html')
	else:
		if request.POST.get('l_register'):
			return HttpResponseRedirect(reverse('register'))
		else:
			username = request.POST.get('username',None)
			password = request.POST.get('password',None)
			userModel = UserModel.objects.filter(username=username, password=password).first()
			if userModel:
				# response = HttpResponseRedirect(reverse('index'))
				# sessionid = str(uuid.uuid4())                       
				# response.set_cookie('myssionid',sessionid)			
				# request.session[sessionid] = userModel.username
				request.session['username'] = userModel.username
				request.session['password'] = userModel.password
				# return response
				return HttpResponseRedirect(reverse('index'))
			else:
			    return HttpResponse(u'用户名或密码错误')

def register(request):
	if request.method == 'GET':
		return render(request,'register.html')
	else:
		form = RegistForm(request.POST,request.FILES)   # request.FILES  上传文件需要
		if form.is_valid():
			username = form.cleaned_data.get('username',None)
			password = form.cleaned_data.get('password',None)
			email = form.cleaned_data.get('email',None)
			repassword = form.cleaned_data.get('repassword',None)
			avatar = form.cleaned_data.get('avatar',None)                   #获取上传的文件
			if password == repassword:
				user = UserModel(username=username, password=password, email=email, avatar=avatar)
				user.save()
				html = 'username:%s, password:%s, email:%s' %(username, password, email)
			return HttpResponse(html)
		else:
			return render(request,'register.html',{'errors':form.errors.as_json()})

















def register_demo(request):
	if request.method == 'GET':
		form = RegistForm()
		return render(request,'register_demo.html', {'form':form})
	else:
		form = RegistForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username',None)
			password = form.cleaned_data.get('password',None)
			email = form.cleaned_data.get('email',None)
			repassword = form.cleaned_data.get('repassword',None)
			if password == repassword:
				user = UserModel(username=username, password=password, email=email)
				user.save()
				html = 'username:%s, password:%s, email:%s' %(username, password, email)
			return HttpResponse(html)
		else:
			return HttpResponse('failure')



