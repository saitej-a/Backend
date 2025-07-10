from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import MessageSerializer
from .models import Message
# Create your views here.
class MessageViewSet(ModelViewSet):
  serializer_class=MessageSerializer
  queryset=Message.objects.all()