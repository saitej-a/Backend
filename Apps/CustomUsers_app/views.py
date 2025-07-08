from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer


User=get_user_model()
class UserViewset(viewsets.ModelViewSet):
	queryset=User.objects.all()
	serializer_class=CustomUserSerializer
	"""def create(self,request):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			user=User.objects.create_user(username=serializer.validated_data['username'],password=serializer.validated_data['password'],role=serializer.validated_data['role'])
			return Response(data={'message':'User created successfully'},status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)"""