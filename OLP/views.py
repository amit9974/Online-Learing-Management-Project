from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import views

def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')
    

def python_developer(request):
    return render(request, 'courses/Python Developer.html')
