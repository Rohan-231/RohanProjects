from django.contrib import admin
from django.urls import path
from rohan import views

urlpatterns = [
    path('', views.index,name='home'),
    path('login',views.loginUser,name="login"),
    path('logout',views.logoutUser,name="logout"),
    path("about",views.about,name = 'about'),
    path("services",views.services,name = 'Services'),
    path("contactus",views.contactus,name = 'contactus'),
]
