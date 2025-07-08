from django.shortcuts import render
from .serializer import FeePaymentSerializer
from rest_framework.viewsets import ModelViewSet
from .models import FeePayment
# Create your views here.
class FeePaymentViewSet(ModelViewSet):
  serializer_class=FeePaymentSerializer
  queryset=FeePayment.objects.all()
  