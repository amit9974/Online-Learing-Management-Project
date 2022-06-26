# from jsonschema import ValidationError
# from app.forms import StudentRegisterForm
# from app.models import Student
# from django.contrib import messages
# from django.shortcuts import render, redirect

# # Student registration
# def Student_Register(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirm_password')
 
#         print(username,first_name,last_name,email)
#         # check email
#         if Student.objects.filter(email=email).exists():
#             messages.warning(request, 'The Email is already Exist')
#             return redirect('student_register')

#         # check username
#         if Student.objects.filter(username=username).exists():
#             messages.warning(request, "This username is already taken")
#             return redirect('student_register')

#         student = Student.objects.create(username=username,first_name=first_name,last_name=last_name,email=email,password=password)

#         if student.password == confirm_password:
#             student.save()
#             return redirect('login')
        
#         else:
#             messages.error("Confirm Password and Password is not matched")
#             return redirect('student_register')
        
        
#     return render(request, 'student_register/student_register.html')