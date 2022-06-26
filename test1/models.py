from django.db import models

# Create your models here.
class user_list(models.Model):
    name = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    age= models.IntegerField()

class zhangrui(models.Model):
    name = models.CharField(max_length=20)