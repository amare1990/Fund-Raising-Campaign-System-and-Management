"""bibugn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# bibugn/urls.py
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from fundraising import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^account/$', views.account, name = 'account'),
    url(r'^$',views.index,name='index'),
    url(r'^special/',views.special,name='special'),
    path('fundraising/',include('fundraising.urls')),
    path('articles/',include('articles.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^signup/$',views.signup, name='signup'),
]
