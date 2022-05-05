from django.db import models
from django import forms
from django.contrib.auth.models import User
# Create your models here.
"""
class User(models.Model):
    user_name = models.CharField(max_length=264)
    user_email = models.EmailField()
    user_password = models.CharField(forms.PasswordInput, max_length=10)
    def __str__(self):
        return self.user_name
"""


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Contact(models.Model):

    name =models.CharField(blank=True, max_length=250)
    email = models.EmailField(blank=True)
    message =models.CharField(blank=True, max_length=10000)

