
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def REGISTER(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check Email
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'This Email is already exist.')
            return redirect('register')

        # Check Username
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'This username is already exist. ')
            return redirect('register')

        user = User(
            username=username,
            email= email,
        )
        user.set_password(password)
        user.save()
        return redirect('login')
 
    return render(request, 'registration/register.html')
