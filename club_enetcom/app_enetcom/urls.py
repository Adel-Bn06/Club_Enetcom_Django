from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView
from .views import YourChatboxView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('compte2/add_membre',add_membre,name='add_membre'),
    path('add_membre/confirmation',confirmation,name='confirme'),
    path('add_pres/',add_pres,name='yourpres'),
    path('add_pres/success',success,name='success'),
    path('base/',base,name='base'),
    path('login/compte',compte,name='compte'),
    path('compte2/logout/', user_logout, name='user_logout'),
    path('compte2/',compte2,name='compte2'),
    path('compte2/actualite',actualite,name='actualites'),
    path('compte2/chatbox',chatbox),
    path('compte2/formation',Formations),
    path('compte2/souvenir',souvenirs),
    path('compte2/profile',profile,name='profile'),
    path('password_change/',PasswordChangeView.as_view(),name='passwor_change'),
    path('password_change/done/',PasswordChangeDoneView.as_view(),name='passwor_change_done'),
    path('compte2/chat/', ChatboxView.as_view(), name='chatbox'),
    path('compte2/parametre',parametre,name='parametre'),
    path('welcome_user/',welcome_user,name='welcome_user'),
    path('welcome_user/<id>',welcome_user,name='welcome_user1'),
   
]
