from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CustomUserSerializer
from .models import CustomUser
# Create your views here.
@api_view(['GET'])
def listUsers(request):
    users=CustomUser.objects.all()
    print(users)
    serialized_data=CustomUserSerializer(users,many=True)
    print(serialized_data.data)
    return Response(data={'users':serialized_data.data},status=200)