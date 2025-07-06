from rest_framework.serializers import Serializer
from .models import CustomUser
class CustomUserSerializer(Serializer):
    class Meta:
        model=CustomUser
        fields=['id', 'username', 'full_name', 'email', 'role']