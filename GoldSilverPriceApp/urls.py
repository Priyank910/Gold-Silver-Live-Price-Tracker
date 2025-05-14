from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('contact', views.contact),
    path('login', views.login),
    path('save-login', views.savelogin),
    path('register', views.register),
    path('save-register', views.saveregister),
    path('gold', views.gold),
    path('silver', views.silver),
]