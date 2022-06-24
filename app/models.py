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
    category = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.category




# Course List Model
class CourseList(models.Model):
    category = models.ForeignKey(CourseCategory,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    fee = models.IntegerField()
    pic = models.FileField(upload_to='Course_pic')
    description = models.TextField(max_length=300)

    def __str__(self) -> str:
        return self.name



