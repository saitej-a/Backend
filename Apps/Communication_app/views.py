from django.shortcuts import render
from .serializer import MessageSerializer,ConversationSerializer 
from .models import Message,Conversation
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def listMessages(request):
  data=Message.objects.filter(conversation__participants=request.user)
  serialized_data=MessageSerializer(data,many=True)
  return Response(data=serialized_data.data,status=status.HTTP_200_OK)
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def createMessage(request):
  serialized_data=MessageSerializer(data=request.data)
  if serialized_data.is_valid():
    serialized_data(sender=request.user)
    serialized_data.save()
    return Response({'message':'Sent message Successfully'},status=status.HTPP_201_CREATED)
  return Response(serialized_data.errors,status=301)