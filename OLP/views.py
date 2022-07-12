from typing import Counter
from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import *
from django.contrib import messages
from django.template.loader import render_to_string
from django.http import JsonResponse


def base(request):
    return render(request, 'base.html')


def home(request):
    category = CourseCategory.objects.all().order_by('id')
    course = CourseList.objects.filter(status='PUBLISH').order_by('-id')
    author = Author.objects.all()
    context = {
        'category':category,
        'course': course,
        'author':author,
    }

    return render(request, 'home.html',context)
    
 
def python_developer(request):
    return render(request, 'courses/Python Developer.html')

# def python_data_science(request):
#     return render(request,'courses/Python DataScience.html')

# def python_django(request):
#     return render(request, 'courses/Python Django.html')

# def node_js(request):
#     return render(request, 'courses/Node Js.html')

# def machine_learning(request):
#     return render(request, 'courses/Machine Learning.html')

# def jquerry(request):
#     return render(request, 'courses/Jquerry.html')

# def javascript(request):
#     return render(request, 'courses/JavaScript.html')

# def html(request):
#     return render(request, 'courses/Html.html')

# def full_stack(request):
#     return render(request, 'courses/Full stack.html')

# def backend(request):
#     return render(request, 'courses/Backend.html')


def course_list(request):
    category = CourseCategory.objects.all().order_by('id')
    course = CourseList.objects.filter(status='PUBLISH').order_by('-id')
    author = Author.objects.all()
    context = {
        'category': category,
        'course': course,
        'author': author,
    }
    return render(request, 'courses/all_course.html',context)



def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        msg = ContactForm.objects.create(name=name,email=email,message=message)
        msg.save()
        messages.success(request,'Your message has been send successfully')
        return redirect('contact-us')
    return render(request, 'contact.html')


def about_us(request):
    return render(request, 'about-us.html')


def my_course(request):
    return render(request,'courses/html.html')

