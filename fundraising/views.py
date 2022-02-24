from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from fundraising.forms import UserForm, WorkerForm, PromiseForm, PayForm
#from fundraising.forms import WorkerForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from fundraising.models import Promise, Pay
#from fundraising.workerforms import WorkerForm
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Sum

#from .models import Pay

from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'Account created successfully')
            #print('Account Created Successfully')
            return redirect('/fundraising/user_login')
    
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request, 'fundraising/signup.html', {'user_form':user_form})

def index(request):
    return render(request,'articles/latest_news.html')
def account(request):
    return render(request,'fundraising/fundraisingregistration.html')
@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'fundraising/fundraisinglogin.html', {})



#@login_required
def add_bio(request):
    #registered = False
    if request.method == 'POST':
        if request.user.is_authenticated:
            #user_form = UserForm(data=request.POST)
            worker_form = WorkerForm(data=request.POST)
            if worker_form.is_valid():
                #user = user_form.save()
                w = worker_form.save()
                w.user = request.user
                w =worker_form.save(commit=False)
                #w.user =user
                w.save()
                #registered = True
                return redirect('index')
            else:
                print(worker_form.errors)
        else:
            return redirect('/fundraising/user_login')
    else:
        #user_form = UserForm()
        worker_form = WorkerForm()
    return render(request, 'fundraising/add_bio.html', {'worker_form': worker_form})

#@login_required    
def promise(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            #user_form = UserForm(data=request.POST)
            promise_form = PromiseForm(data=request.POST)          
            if promise_form.is_valid():               
                p = promise_form.save()
                p.user = request.user
                p =promise_form.save(commit=False)
                p.save()
                #registered = True
                messages.success(request, 'You promise was done successfully!')
                return redirect('index')
            else:                
                print(promise_form.errors)
        else:
            return redirect('/fundraising/user_login')
    else:
        #user_form = UserForm()
        promise_form = PromiseForm()    
    return render(request, 'fundraising/promise.html', {'promise_form': promise_form})


#Fundraising Payment
#@login_required    
def pay(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            #user_form = UserForm(data=request.POST)
            #pay_form = PayForm(data=request.POST)
            pay_form = PayForm(request.POST, request.FILES)
            #if user_form.is_valid() and pay_form.is_valid():
            if pay_form.is_valid():
                #user = user_form.save() 
                pay =pay_form.save(commit=False)
                #pay = pay_form.save()
                pay.user = request.user               
                #pay_form.save()
                #pay.user =user
                pay.save()
                #registered = True
                return redirect('index')
            else:
               #print(user_form.errors, pay_form.errors)
                print(pay_form.errors)
        else:
            return redirect('/fundraising/user_login')
    else:
        #user_form = UserForm()
        pay_form = PayForm()
    return render(request, 'fundraising/pay.html', {'pay_form': pay_form})



# after updating it will redirect to detail_View 
def detail_view(request): 
    # dictionary for initial data with  
    # field names as keys 
    user = request.user
    context ={} 
   
    # add the dictionary during initialization 
    context["data"] = Promise.objects.get(user = user) 
           
    return render(request, "fundraising/detail_view.html", context) 
  
# update view for details 
# update view for details
"""
def update_view(request, id): 
    # dictionary for initial data with  
    # field names as keys 
    #user = request.user
    context ={} 
  
    # fetch the object related to passed id 
    obj = get_object_or_404(Promise, id = request.user.username) 
  
    # pass the object as instance in form 
    form = PromiseForm(request.POST or None, instance = obj) 
  
    # save the data from the form and 
    # redirect to detail_view 
    if form.is_valid(): 
        form.save() 
        #return HttpResponseRedirect("/"+id) 
  
    # add form dictionary to context 
    context["form"] = form 
  
    return render(request, "fundraising/update_view.html", context) """

def update_view(request): 
    # dictionary for initial data with  
    # field names as keys 
    #user = request.user
    context ={} 
  
    # fetch the object related to passed id 
    #obj = get_object_or_404(Promise, request.user)
    obj = Promise.objects.get(user = request.user)
  
    # pass the object as instance in form 
    form = PromiseForm(request.POST or None, instance = obj) 
  
    # save the data from the form and 
    # redirect to detail_view 
    if form.is_valid(): 
        form.save() 
        return HttpResponseRedirect("/fundraising/detail_view") 
  
    # add form dictionary to context 
    context["form"] = form 
  
    return render(request, "fundraising/update_view.html", context) 

#Total Amount of Promised
def total_promise(request):
    context = {}
    #total_promised = Promise.objects.all().aggregate(Sum('amount_in_ETB'))
    total_promised = list(Promise.objects.aggregate(Sum('amount_in_ETB')).values())[0]
    context["data"] = total_promised
    return render(request, "fundraising/total_promise.html", context)
#Total Amount of Payment till now
def total_payment(request):
    context = {}
    #total_paid = Pay.objects.all().aggregate(Sum('amount_in_ETB'))
    total_paid = list(Pay.objects.aggregate(Sum('amount_in_ETB')).values())[0]
    context["data"] = total_paid
    return render(request, "fundraising/total_payment.html", context)

#view all Promises here
def view_total_promise(request):
    p = Promise.objects.all()
    context = {'p':p}
    return render(request, "fundraising/view_total_promise.html", context)

#view all Payments here
def view_total_payment(request):
    p = Pay.objects.all()
    context = {'p':p}
    return render(request, "fundraising/view_total_payment.html", context)

#export Promises into pdf
from reportlab.pdfgen import canvas  
#from django.http import HttpResponse  
#from django.core import serializers    
def getpdf_promise_total(request):  
    response = HttpResponse(content_type='application/pdf')  
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'
    p = canvas.Canvas(response) 
    details =  list(Promise.objects.all().values())[0]
    #result = serializers.serialize("xml", details)
    result = str(details)
    #print details
    
    p.setFont("Times-Roman", 10)  
    #p.drawString(100,700, "Hello, Javatpoint.")  
    p.drawString(100, 800, result)
    p.showPage()  
    p.save()  
    return response  
   
