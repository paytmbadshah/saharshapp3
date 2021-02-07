from django.db import models

# Create your models here.

class user_data(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    phone = models.CharField(max_length=250,null=True)
    gender = models.CharField(max_length=250,null=True)
    age = models.CharField(max_length=250,null=True)