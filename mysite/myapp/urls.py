from django.shortcuts import render
from django.urls import path
from myapp.views import home_view

urlpatterns = [
    path('',home_view, name='homepage')
]
