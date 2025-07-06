from django.urls import path
from .views import listUsers
url_patterns=[
    path('',listUsers)
]