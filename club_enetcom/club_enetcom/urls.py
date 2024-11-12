"""
URL configuration for club_enetcom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.contrib.admin import AdminSite
from django.urls import path
from app_enetcom.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordChangeDoneView,PasswordChangeView

urlpatterns = [
    path('admin/',AdminSite().urls),
    path('compte2/add_membre',add_membre,name='add_membre'),
    path('add_membre/confirmation',confirmation,name='confirme'),
    path('add_pres/',add_pres,name='yourpres'),
    path('add_pres/success',success,name='success'),
    path('base/',base,name='base'),
    path('compte2/logout/', user_logout, name='user_logout'),
    path('compte2/<id>',compte2,name='compte2'),
    path('compte2/chatbox',chatbox),
    path('compte2/formation',Formations),
    path('compte2/souvenir',souvenirs),
    path('compte2/profile',profile,name='profile'),
    path('password_change/',PasswordChangeView.as_view(),name='password_change'),
    path('password_change/done/',PasswordChangeDoneView.as_view(),name='password_change_done'),
    path('compte2/chat/', ChatboxView.as_view(), name='chatbox'),
    path('compte2/parametre',parametre,name='parametre'),
    path('welcome_user/',welcome_user,name='hello_user'),
    path('welcome_user/<id>',welcome_user,name='welcome_user1'),
   
]
