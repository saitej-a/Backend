from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    Role_CHOICES = [
        ('T', 'Teacher'),
        ('A', 'Admin'),
        ('S', 'Student'),
    ]
    Role=models.CharField(max_length=25,choices=Role_CHOICES)
