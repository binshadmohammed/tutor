from django.db import models

# Create your models here.

class teacher_register(models.Model):
    name=models.CharField(max_length=200)
    age=models.CharField(max_length=200)
    qualification=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    experience=models.CharField(max_length=200)
    fee=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    place=models.CharField(max_length=200)
    mobile=models.CharField(max_length=200)
    password1=models.CharField(max_length=200)
    password2=models.CharField(max_length=200)
    image=models.ImageField(max_length=300)
    approvedsts=models.CharField(max_length=200)