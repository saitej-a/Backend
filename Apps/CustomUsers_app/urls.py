from django.urls import path,include
from .views import UserViewset, dashboard, register
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register(r'users',UserViewset)
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
url_patterns=[
  path('',include(router.urls)),
  path('register/',register),
  path('dashboard/',dashboard),
  path('token/',TokenObtainPairView.as_view()),
  path('token/refresh/',TokenRefreshView.as_view())
]