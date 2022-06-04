from django.conf.urls import url
from .views import register,login, authenticate
from django.urls import path


app_name = 'user'

urlpatterns = [

#    url(r'^signup$',register),
#    url(r'^signin$',login)
    path('signup',register),
    path('signin',login),
    path('',authenticate)

]
