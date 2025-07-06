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
