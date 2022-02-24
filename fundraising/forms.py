#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 17:03:05 2020

@author: hamel
"""

from django import forms
#from fundraising.models import Worker
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from fundraising.models import Promise, Pay, Worker

class UserForm(UserCreationForm):
    #email = forms.EmailField(required =false, max_length=100, help_text='Required')
    class Meta():
        model = User
        fields = ('username','password1', 'password2')
        
class PromiseForm(forms.ModelForm):
    class Meta():
        model = Promise
        fields= '__all__'
        #exclude=('user',)
        
        
class PayForm(forms.ModelForm):
    class Meta():
        model = Pay
        fields= '__all__'  
    
class WorkerForm(forms.ModelForm):
    class Meta():
        model = Worker
        fields= '__all__'
        #exclude=('user',)
        
        
