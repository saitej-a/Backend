from django.db import models
from ..CustomUsers_app.models import CustomUser
# Create your models here.
class FeePayment(models.Model):
    student=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    purpose=models.TextField()
    paid=models.BooleanField(default=False)
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.student} - {self.amount} - {self.purpose[:20]}'
