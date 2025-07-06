from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomUserSerializer
from .models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(['GET'])
def listUsers(request):
    users = User.objects.all()
    serializer = CustomUserSerializer(users, many=True)
    return Response({'users': serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def getUser(request, pk):
    try:
        user = User.objects.get(pk=pk)
        serializer = CustomUserSerializer(user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def createUser(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'message': 'Username and password required'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'message': 'Username already exists'}, status=status.HTTP_409_CONFLICT)

    user = User.objects.create_user(username=username, password=password)
    user.save()

    return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def deleteUser(request, pk):
    auth_user_id = request.data.get('auth_user')

    try:
        auth_user = User.objects.get(id=auth_user_id)
        if not auth_user.is_superuser:
            return Response({'message': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

        user_to_delete = User.objects.get(id=pk)
        user_to_delete.delete()
        return Response({'message': 'User deleted successfully'}, status=status.HTTP_202_ACCEPTED)

    except User.DoesNotExist:
        return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
