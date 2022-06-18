from django.db import models

# Create your models here.

class add_user(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.IntegerField()
    