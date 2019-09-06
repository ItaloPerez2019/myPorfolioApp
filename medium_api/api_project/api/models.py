from django.db import models

# Create your models here.

class UserInformation(models.Model):
    name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    age = models.Field(max_length=100)