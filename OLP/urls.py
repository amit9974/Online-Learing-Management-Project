"""OLP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from . import views
from . import user_login, student_login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/',include('app.urls')),
    path('',views.home, name='home'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/register',user_login.REGISTER,name='register'),
    path('contact-us/', views.contact_us, name='contact-us'),
    path('doLogin/', user_login.doLogin, name='doLogin'),
    path('course_list/', views.course_list, name='course_list'),
    path('about-us/', views.about_us, name='about-us'),
    path('profile/', user_login.profile, name='profile'),
    path('accounts/profile/update', user_login.profile_update, name='profile_update'),
    path('my_course/', views.my_course, name= 'my_course'),
    path('search/', views.search_course, name='search_course'),
    path("course_details/<slug>/",views.course_details,name="course_details"),



    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



