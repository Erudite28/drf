from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('project', views.Wordcounter, name='Wordcounter'),
    path('counter', views.counter, name='counter'),
    path('index2', views.index2, name='index2'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]