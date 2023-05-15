from django.urls import  path
from . import  views

urlpatterns=[
    path('',views.home,name="home"),
    path('loguser',views.loguser,name="loguser"),
    path('userlogout',views.userlogout,name="userlogout"),
    path('about',views.About,name="about"),

]