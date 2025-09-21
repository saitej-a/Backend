from django.db import models

# Create your models here.

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
