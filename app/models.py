from asyncio.windows_events import NULL
from distutils.command.build import build
from django.db import models
# Create your models here.

# Contact Form Model
class ContactForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.email



# Course Category Model
class CourseCategory(models.Model):
    icon = models.FileField(upload_to='Media/Course_Icon', null=True)
    name = models.CharField(max_length=100, null=True, default=NULL)

    def __str__(self) -> str:
        return self.name


# Author Model
class Author(models.Model):
    author_profile = models.ImageField(upload_to='Media/author')
    name = models.CharField(max_length=100, null=True)
    about_author = models.TextField(max_length=300)

    def __str__(self) -> str:
        return self.name



# Course List Model
class CourseList(models.Model):
    STATUS = (
        ('PUBLISH','PUBLISH'),
        ('DRAFT', 'DRAFT'),
    )
    
    image = models.ImageField(upload_to="Media/featured_img", null=True)
    video = models.CharField(max_length=200,null=True)
    title = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, null=True)
    description =models.TextField(max_length=400)
    price = models.IntegerField(null=True)
    discount = models.IntegerField(null=True)
    slug = models.SlugField(default='',max_length=500,null=True,blank=True)
    status = models.CharField(choices=STATUS,max_length=100,null=True)

    def __str__(self) -> str:
        return self.title




# Students
class Student(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name