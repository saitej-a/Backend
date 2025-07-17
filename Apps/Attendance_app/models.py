from django.db import models
from Apps.CustomUsers_app.models import CustomUser  

class Attendance(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=100)
    date = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=[('Present', 'Present'), ('Absent', 'Absent')],
        default='Present'
    )

    def __str__(self):
        return f"{self.user} | {self.class_name} | {self.date} | {self.status}"



