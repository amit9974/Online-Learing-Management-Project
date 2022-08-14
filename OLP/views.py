from multiprocessing import reduction
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from cart.cart import Cart



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
    category = CourseCategory.objects.all().order_by('id')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        msg = ContactForm.objects.create(name=name,email=email,message=message)
        msg.save()
        messages.success(request,'Your message has been send successfully')
        return redirect('contact-us')

    context = {
        'category':category,
    }
    return render(request, 'contact.html',context)


def about_us(request):
    category = CourseCategory.objects.all().order_by('id')
    context = {
        'category':category,
    }
    return render(request, 'about-us.html', context)


def my_course(request):
    return render(request,'courses/html.html')

def enroll_course(request, slug):
    course = CourseList.objects.filter(slug=slug)
    category = CourseCategory.objects.all().order_by('id')

    context ={
        'course':course,
        'category':category,
    }
    return render(request, 'courses/enroll_course.html', context)


def search_course(request):
    query = request.GET['query']
    course = CourseList.objects.filter(title__icontains = query)
    category = CourseCategory.objects.all().order_by('id')
   
    context = {
        'course':course,
        'category':category,
    }
    return render(request, 'search/search.html',context)


# @login_required(login_url='/accounts/login')
def course_details(request, slug):
    course = CourseList.objects.filter(slug = slug)
    author = Author.objects.all()
    all_course = CourseList.objects.all()
    category = CourseCategory.objects.all().order_by('id')

  
    context = {
        'course': course,
        'author':author,
        'all_course':all_course,
        'category':category,

        }
    return render(request, 'courses/course_details.html', context)



def page_404(request):
    return render(request, 'error/404.html')


def cart(request):
    category = CourseCategory.objects.all().order_by('id')
    context = {
        'category':category,
    }
    return render(request, 'cart/cart.html',context)

