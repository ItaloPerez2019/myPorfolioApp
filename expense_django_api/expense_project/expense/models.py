from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth
from django.urls import reverse
# Create your models here.


# class User(models.Model):
#
#     username = models.CharField(max_length=50, unique=True)
#     email = models.EmailField(max_length=75, unique=True)
#     password = models.CharField(max_length=100)
#
#     # def __init__(self, username, password):
#     #     self.username = username
#     #     self.password = password
#
#     # def __init__(self, email, password):
#     #     self.email = email
#     #     self.password = password
#
#     @property
#     def is_user_login(self, request):
#         user_login = 'not_login'
#         if request.session['role'] == 'user_login':
#             user_login = 'user_login'=
#         return user_login
#
#     def __str__(self):
#         return self.username





class UserLogin(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)

    class Meta:
        managed = False


class Expense(models.Model):
    UTILITY = 'U'
    GROCERY = 'G'
    RESTAURANT = 'R'
    T_TYPES = (
        ('U', 'Utility'),
        ('G', 'Grocery'),
        ('R', 'Restaurants')
    )

    user = models.ForeignKey(User, related_name='expense', on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    types = models.CharField(max_length=1, choices=T_TYPES, default=GROCERY)

