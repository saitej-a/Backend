from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes,api_view
from .permissions import IsAdmin,IsParent,IsStudent,IsTeacher,IsTeacherOrAdmin
import random
from django.core.mail import send_mail
from .models import passwordTokens
from django.conf import settings
User=get_user_model()
class UserViewset(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = [IsTeacherOrAdmin]

    
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
def generateToken(request):
    """{"user_id":1,"e-mail":"ankamsaiteja27@gmail.com"} 
    user receives email to change the password"""
    user_id=request.data.get('user_id')
    mail=request.data.get('e-mail')
    chars=[chr(ord('A')+i) for i in range(26)]
    chars.extend([chr(ord('a')+i) for i in range(26)])
    chars.extend([str(i) for i in range(10)])
    token=random.choices(chars,k=32)
    token=''.join(token)
    try:
        user=User.objects.get(id=user_id)
    except:
        return Response({'message':'User doesn\'t exists'},status=status.HTTP_404_NOT_FOUND)
    reset_obj=passwordTokens.objects.create(user=user,token=token)
    reset_link=request.build_absolute_uri(f'/api/password_reset/{reset_obj.token}/')
    #send email
    subject = 'Password Reset Request'
    message = f'Your password reset token is: {reset_link}'
    msg='Successfully sent the email'
    sts=status.HTTP_200_OK
    try:
        send_mail(subject, message,settings.EMAIL_HOST_USER, [mail], fail_silently=False)
    except Exception as e:
        return Response({'message': f'Error sending email: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({'message':message},status=sts)

@api_view(['POST'])
def passwordReset(request,pk):
    new_password=request.data.get('new_password')
    try:
        tokenObject=passwordTokens.objects.get(token=pk)
    except passwordTokens.DoesNotExist:
        return Response({'message':'You are not authorized to view this'},status=status.HTTP_403_FORBIDDEN)
    if new_password:
        tokenObject.user.set_password(new_password)
        tokenObject.delete()
        return Response({'message':'Password reset successfully'},status=status.HTTP_202_ACCEPTED)
    else:
        return Response({'message':'Password is required'},status=status.HTTP_400_BAD_REQUEST)
    