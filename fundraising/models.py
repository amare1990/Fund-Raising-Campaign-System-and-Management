#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 16:27:59 2020

@author: hamel
"""

from django.db import models
from django.contrib.auth.models import User
#from datetime import date


highest_degree = ((0, "PhD"),
                  (1, "MSc"),
                  (2, "MA"),
                  (3, "BA"),
                  (4, "Bsc."),
                  (5, "Diploma"),
                  (6, "Certificate")
                  )

class Worker(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, unique=True, primary_key=True)
    full_name = models.CharField(max_length = 100, default="")   
    sex = models.CharField(max_length = 100, default="")
    #email = models.EmailField(blank=True, null=True)
    #tell_no = models.DecimalField(max_digits = 14, decimal_places = 5, default =0913455645)
    place_of_birth = models.CharField(max_length = 100, default="")
    title = models.CharField(max_length = 100, default="")
    primary_school = models.CharField(max_length = 100, default="")
    secondary_school= models.CharField(max_length = 100, blank=True, null=True)
    #education = models.CharField(max_length = 100, choices=highest_degree, default= 4)
    #bussiness_men = models.BooleanField(choices= bussiness_men, default =bussiness_men.1)
    #phd = models.CharField(max_length = 100, blank=True, null=True)
    #msc = models.CharField(max_length = 100, blank=True, null=True)
    #bsc= models.CharField(max_length = 100, blank=True, null=True)
    job= models.CharField(max_length = 100, default="")
    city = models.CharField(max_length = 100, default="Addis Ababa")
    stateOrProvince = models.CharField(max_length = 100, blank=True, null=True)
    country = models.CharField(max_length = 100, blank=True, null=True, default = 'Ethiopia')
    def __str__(self):
        return self.user.username
    
    
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
    
class Promise(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, unique=True, primary_key=True)
    full_name_promise = models.CharField(max_length = 100, default ="")
    on_behalf_of = models.CharField(max_length = 100, default ="")
    amount_in_ETB = models.DecimalField(max_digits=14, decimal_places =5)
    created_on = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    #updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    def __str__(self):
        return self.user.username    
 
    
class Pay(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, unique=True, primary_key=True)
    full_name_pay = models.CharField(max_length = 100, default ="")
    on_behalf_of = models.CharField(max_length = 100, default ="")
    amount_in_ETB = models.DecimalField(max_digits=14, decimal_places =5)
    created_on = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    #updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    upload_receit = models.ImageField(upload_to='fundraising/paid_receits')
    
    def __str__(self):
        return self.user.username  
        
       
