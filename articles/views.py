#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:20:16 2020

@author: hamel
"""

from django.views import generic
#from articles.models import Post


from .models import Post
from articles.forms import CommentForm, PostForm
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'articles/articlespost_list.html'

def post_detail(request, slug):
    template_name = 'articles/articlespost_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

# functions to get Users post
def post(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            #user_form = UserForm(data=request.POST)
            post_form = PostForm(data=request.POST)
            if post_form.is_valid():
                #user = user_form.save()
                post = post_form.save()
                post.author = request.auther
                post = post_form.save(commit=False)
                #w.user =user
                post.save()
                #registered = True
                messages.success(request, 'Your article was posted successfully!')
                return redirect('index')
            else:
                print(post_form.errors)
        else:
            return redirect('/fundraising/user_login')
    else:
        #user_form = UserForm()
        post_form = PostForm()
    return render(request, 'articles/post.html', {'post_form': post_form})
