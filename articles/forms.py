#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 12:04:33 2020

@author: hamel
"""

from django import forms
from articles.models import Post

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields= '__all__'
        prepopulated_fields = {'slug': ('title',)}
        
        
from .models import Comment
#from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')