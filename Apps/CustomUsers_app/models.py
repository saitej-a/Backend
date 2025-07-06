from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    Role_CHOICES = [
        ('TEACHER', 'Teacher'),
        ('ADMIN', 'Admin'),
        ('STUDENT', 'Student'),
    ]
    role=models.CharField(max_length=25,choices=Role_CHOICES)

