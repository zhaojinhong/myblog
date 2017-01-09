# -*- coding: utf-8 -*-
# @Author: zhaojinhong
# @Date:   2016-12-14 10:28:25
# @Last Modified by:   zhaojinhong
# @Last Modified time: 2017-01-06 10:04:04
"""douban URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
#from django.contrib import admins
from books import views

urlpatterns = [
    # url(r'^admin/$', admin.site.urls),
    url(r'^index/$', views.index, name='index'),
    url(r'^delete/$', views.delete_books),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register_demo/$', views.register_demo, name='register_demo')
    #为article的url命名为books_article
    # url(r'^article/(?P<article_id>\d+)$', views.article, name='books_article'),
]