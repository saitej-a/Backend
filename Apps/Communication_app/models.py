from django.db import models
from ..CustomUsers_app.models import CustomUser


# Create your models here.
class Message(models.Model):
    sender=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    receiver=models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='receiver')
    body=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.body


# Announcements model
class Announcement(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

#Feedback model
from django.conf import settings

class Feedback(models.Model):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('parent', 'Parent'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    ]

    title = models.CharField(max_length=100)
    message = models.TextField()
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.role} - {self.created_at.strftime('%Y-%m-%d')}"
