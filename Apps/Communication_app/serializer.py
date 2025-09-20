from rest_framework.serializers import ModelSerializer
from .models import Message,Conversation
from .models import Announcement


class MessageSerializer(ModelSerializer):
	class Meta:
		model=Message
		fields='__all__'

class ConversationSerializer(ModelSerializer):
	class Meta:
		model=Conversation
		fields="__all__"

class AnnouncementSerializer(ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'

