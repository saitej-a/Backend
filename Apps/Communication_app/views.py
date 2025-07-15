from django.shortcuts import render
from .serializer import MessageSerializer,ConversationSerializer 
from .models import Message,Conversation
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import MethodNotAllowed
from django.contrib.auth import get_user_model

User=get_user_model()

class ConversationViewSet(ModelViewSet):
    serializer_class=ConversationSerializer
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        return Conversation.objects.filter(participants=self.request.user)
    def perform_create(self, serializer):
        convo=serializer.save()
        convo.participants.add(self.request.user)
    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed('UPDATE')
    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed('UPDATE')
    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed('DELETE')
    def retrieve(self, request, *args, **kwargs):
        pk=kwargs['pk']
        convo=Conversation.objects.filter(id=pk)
        if convo:
            data=Conversation.objects.get(id=pk)
            serializedData=ConversationSerializer(data)
            return Response(data=serializedData.data,status=status.HTTP_200_OK)
        else:
            return Response({"message":"Not Authorized to View this"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    @action(detail=True,methods=['POST'])
    def add_participant(self,request,pk=None):
        user_id=request.data.get('participants')
        if Conversation.objects.filter(id=pk).exists():

            obj=Conversation.objects.get(id=pk)
            if obj.participants.filter(id=request.user.id).exists():
                obj.participants.add(user_id)
                return Response(data={'message':'Successfully User added',"data":ConversationSerializer(obj).data},status=status.HTTP_201_CREATED)        
            else:
                return Response({"message":"You are not Authorized to make this changes"},status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({'message':'No Conversations Exists'},status=status.HTTP_404_NOT_FOUND)
        
    @action(detail=True,methods=['POST'])
    def remove_participant(self,request,pk=None):
        user_id=request.data.get('participants')
        obj=Conversation.objects.get(id=pk)
        if obj.participants.filter(id=request.user.id).exists():
            obj.participants.remove(user_id)
            return Response({"message":"Successfully removed the user","data":ConversationSerializer(obj).data},status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"message":"You are not Authorized to do this"},status=status.HTTP_403_FORBIDDEN)
        
class MessageViewSet(ModelViewSet):
    serializer_class=MessageSerializer
    queryset=Message.objects.all()
    permission_classes=[IsAuthenticated]
    def list(self, request, *args, **kwargs):
        if request.user.role == 'ADMIN' or request.user.role=='TEACHER':
            return super().list(request, *args, **kwargs)
        return Response(data={'message':'You are not authorized to view this'},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    def retrieve(self,request,pk):
        """
        Retrives messages in conversation id
        """
        try:
            Conversation.objects.get(id=pk)
        except Conversation.DoesNotExist:
            return Response({'message':'Conversation does no exists'},status=status.HTTP_404_NOT_FOUND)
        
        data=Message.objects.filter(conversation=pk).order_by('timestamp')
        serializedData=MessageSerializer(data,many=True)
        return Response(serializedData.data,status=status.HTTP_200_OK)
    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed('POST')
    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed('PUT')
    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed('DELETE')
    @action(detail=False,methods=['POST'])
    def send_message(self,request):
        copydata=request.data.copy()
        copydata['sender']=request.user.id
        receiver=copydata.get('receiver')
        chat_id=copydata.get('conversation')
        if not (receiver and chat_id):
            return Response({'message':'Conversation and Receiver required'},status=status.HTTP_400_BAD_REQUEST)
        try :
            chat=Conversation.objects.get(id=chat_id)
        except Conversation.DoesNotExist:
            return Response({'message':'No conversation exists'},status=status.HTTP_404_NOT_FOUND)
        if not (chat.participants.filter(id=request.user.id).exists() and chat.participants.filter(id=receiver).exists()):
            return Response({'message':'Can\'t send Message to Non-participant'},status=status.HTTP_403_FORBIDDEN)
        obj=MessageSerializer(data=copydata)
        if obj.is_valid():
            obj.save()
            return Response(obj.data,status=status.HTTP_201_CREATED)
        return Response(obj.errors,status=status.HTTP_400_BAD_REQUEST)
    @action(detail=True,methods=['PUT'])
    def read_message(self,request,pk=None):
        try:
            message=Message.objects.get(id=pk)
        except Message.DoesNotExist:
            return Response({'meesage':'Not found'},status=status.HTTP_404_NOT_FOUND)
        read_status=request.data.get('is_read')
        message.is_read= True if read_status == 'true' else False
        message.save()

        return Response(MessageSerializer(message).data,status=status.HTTP_200_OK)