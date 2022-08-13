from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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

def search_course(request):
    query = request.GET['query']
    course = CourseList.objects.filter(title__icontains = query)
    context = {
        'course':course
    }
    return render(request, 'search/search.html',context)

@login_required(login_url='/accounts/login')
def course_details(request, slug):
    course = CourseList.objects.filter(slug = slug)
    author = Author.objects.all()
    all_course = CourseList.objects.all()
    context = {
        'course': course,
        'author':author,
        'all_course':all_course,
    }
    return render(request, 'courses/course_details.html', context)





