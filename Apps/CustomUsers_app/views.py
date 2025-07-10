from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import permission_classes,api_view

User=get_user_model()
class UserViewset(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard(request):
	return Response(data={'message':f'Hello {request.user.username}'},status=status.HTTP_200_OK)
@api_view(['POST'])
def register(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Successfully Created"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def login(request):
  pass