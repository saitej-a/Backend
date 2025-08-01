from django.db import models
from ..CustomUsers_app.models import CustomUser
# Create your models here.
class Conversation(models.Model):
  participants=models.ManyToManyField(CustomUser)
  created_at=models.DateTimeField(auto_now_add=True)
  def __int__(self):
    return self.id
class Message(models.Model):
    conversation=models.ForeignKey(Conversation,on_delete=models.CASCADE)
    sender=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    receiver=models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='receiver')
    body=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    is_read=models.BooleanField(default=False)
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

