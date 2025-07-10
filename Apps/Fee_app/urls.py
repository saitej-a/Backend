from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import FeePaymentViewSet
router=DefaultRouter()
router.register(r'fee',FeePaymentViewSet)
url_patterns=[
  path('',include(router.urls))
]