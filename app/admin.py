from ast import Or
from django.contrib import admin
from .models import *
# Register your models here.

class Lesson_TabularInLine(admin.TabularInline):
    model = Lesson

class Video_TabularInLine(admin.TabularInline):
    model = Video

class course_admin(admin.ModelAdmin):
    inlines = (Lesson_TabularInLine, Video_TabularInLine)

# admin.site.register(Course_list)

admin.site.register(CourseCategory)
admin.site.register(CourseList, course_admin)
admin.site.register(Author)
admin.site.register(ContactForm)
admin.site.register(Order)
admin.site.register(Lesson)
admin.site.register(Video)





