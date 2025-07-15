from django.urls import path,include
from .views import  ConversationViewSet,MessageViewSet
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register(r'conversation',ConversationViewSet,basename='conversation')
router.register(r'messages',MessageViewSet,basename='message')
url_patterns=[
path('',include(router.urls))
]