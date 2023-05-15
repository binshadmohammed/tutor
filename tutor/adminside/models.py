from django.db import models

# Create your models here.


class app_review(models.Model):
    name=models.CharField(max_length=200)
    user=models.CharField(max_length=200)
    message=models.CharField(max_length=200)
    r_date=models.CharField(max_length=200)