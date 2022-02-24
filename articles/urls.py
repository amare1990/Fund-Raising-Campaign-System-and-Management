#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:21:19 2020

@author: hamel
"""

#from . import views
from django.urls import path

from django.conf.urls import url
from articles import views
# SET THE NAMESPACE!
app_name = 'articles'

urlpatterns = [
    url(r'^post/$', views.post, name = 'post'),
    path('post_list/', views.PostList.as_view(), name='post_list'),
    #url(r'^register/$',views.register,name='register'),
    #path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', views.post_detail, name='post_detail')    
    #path('post/', views.post, name='post'),
]