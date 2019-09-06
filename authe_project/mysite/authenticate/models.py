from django.db import models


# Create your models here.

class UserName(models.Model):
    profession = models.CharField(max_length=100)
   

    def __str__(self):
        return '%s' % (self.profession)