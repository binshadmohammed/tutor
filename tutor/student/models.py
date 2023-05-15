from django.db import models

# Create your models here.


class student_register(models.Model):
    name=models.CharField(max_length=200)
    age=models.CharField(max_length=200)
    sclass=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    place=models.CharField(max_length=200)
    password1=models.CharField(max_length=200)
    password2=models.CharField(max_length=200)


class booking(models.Model):
    t_id=models.CharField(max_length=200)
    tname=models.CharField(max_length=200)
    tfee=models.CharField(max_length=200)
    tplace=models.CharField(max_length=200)
    tmobile=models.CharField(max_length=200)
    s_id=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    place=models.CharField(max_length=200)
    sclass=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    topic=models.CharField(max_length=200)
    mobile=models.CharField(max_length=200)
    date=models.CharField(max_length=200)
    s_time=models.CharField(max_length=200)
    e_time=models.CharField(max_length=200)
    status=models.CharField(max_length=200)

class comments(models.Model):
    s_id=models.CharField(max_length=200)
    t_id=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    message=models.CharField(max_length=200)
    sdate=models.CharField(max_length=200)


