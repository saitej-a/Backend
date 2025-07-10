from django.db import models

# Create your models here.    
class ClassRoom(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class_teacher = models.ForeignKey(
        'users.Teacher', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='classrooms'
    )
    subjects = models.ManyToManyField(
        'academics.Subject', 
        on_delete=models.CASCADE,
        blank=True,
        related_name='classrooms'
    )
    students = models.ManyToManyField(
        'users.Student', 
        on_delete=models.CASCADE,
        related_name='classrooms', 
        blank=True
    )
    