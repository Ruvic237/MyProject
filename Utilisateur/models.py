import os.path

from django.db import models
from django.contrib.auth.forms import User
from django.contrib.auth.models import AbstractUser


# A Class Form
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=150, blank=True)
    photo = models.ImageField(upload_to='user_prof')

    student = 'student'
    teacher = 'teacher'

    type_user = [
        (student, 'student'), (teacher, 'teacher')
    ]

    type_profile = models.CharField(max_length=100, choices=type_user, default=student)

    def __str__(self):
        return f'{self.user.username}'









