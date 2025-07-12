from django.urls import path,include
from .views import listMessages, createMessage

url_patterns=[
path('messages/',listMessages),
path('messages/',createMessage)
]