from django.urls import path
from .views import listUsers,getUser,createUser,deleteUser
url_patterns=[
    path('',listUsers),
    path('<int:pk>/',getUser),
    path('create/',createUser),
    path('delete/<int:pk>',deleteUser)
]