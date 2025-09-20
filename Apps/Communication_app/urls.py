from django.urls import path,include
from .views import  ConversationViewSet,MessageViewSet
from rest_framework.routers import DefaultRouter
from .views import AnnouncementViewSet
router=DefaultRouter()
router.register(r'messages',MessageViewSet,basename='message')
router.register(r'announcements', AnnouncementViewSet, basename='announcement')

url_patterns=[
path('',include(router.urls))
]