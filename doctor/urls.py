from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    
    path('/',views.adminhome),
    path('/add/',views.add),
    path('/chat/',views.chat),
    path('/message/',views.message),
    path('/dloc/',views.dloc),
]
