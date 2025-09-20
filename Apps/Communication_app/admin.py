from django.contrib import admin
from .models import Announcement, Message

# Register your models here.
admin.site.register(Message)
admin.site.register(Announcement)
