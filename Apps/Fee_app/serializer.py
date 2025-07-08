from rest_framework.serializers import ModelSerializer
from .models import FeePayment

class FeePaymentSerializer(ModelSerializer):
  class Meta:
    model=FeePayment
    fields=['id', 'student','amount','purpose','paid']