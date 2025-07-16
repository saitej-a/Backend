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
from django.contrib.auth import get_user_model
User=get_user_model()
class passwordTokens(models.Model):
    token=models.CharField(max_length=32,unique=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.token