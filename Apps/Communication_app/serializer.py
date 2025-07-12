from rest_framework.serializers import ModelSerializer
from .models import Message,Conversation

class MessageSerializer(ModelSerializer):
	class Meta:
		model=Message
		fields='__all__'
		read_only_fields=['id','sender','timestamp']
class ConversationSerializer(ModelSerializer):
  class Meta:
    model=Conversation
    fields="__all__"