from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from app.EmailBackend import EmailBackend
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

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





def doLogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = EmailBackend.authenticate(request,
                                        username=email,
                                        password=password)
        
        if user!=None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Email or Password is Incorrct!')
            return redirect('login')
    

def profile(request):
    return render(request, 'profile.html')



def profile_update(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        user_id = request.user.id
        print(user_id)

        user = User.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username


        if password !=None and password != "":
            user.set_password(password)
        user.save()
        messages.success(request, "Profile has been updated successfully! ")
        return redirect('profile')


