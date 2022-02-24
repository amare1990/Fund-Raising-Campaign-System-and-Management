#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 16:38:11 2020

@author: hamel
"""
# fundraising/urls.py
from django.urls import path
from django.conf.urls import url
from fundraising import views
#from .views import detail_view, update_view
# SET THE NAMESPACE!
app_name = 'fundraising'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^add_bio/$',views.add_bio,name='add_bio'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^promise/$', views.promise, name = 'promise'),
    url(r'^pay/$', views.pay, name = 'pay'),
    
    path('detail_view/', views.detail_view, name = 'detail_view' ), 
    #path('<p>/update', views.update_view, name = 'update_view' ),
    path('update/', views.update_view, name = 'update_view' ),
    path('total_promise/', views.total_promise, name = 'total_promise' ),
    path('total_payment/', views.total_payment, name = 'total_payment' ),
    path('view_total_promise/', views.view_total_promise, name = 'view_total_promise'), 
    path('view_total_payment/', views.view_total_payment, name = 'view_total_payment'),
    path('getpdf_promise_total/', views.getpdf_promise_total, name = 'getpdf_promise_total'),
    
   
]