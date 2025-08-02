from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User



    
   
from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('validated', 'Validated'),
        ('awaiting_dispatch', 'Awaiting Dispatch'),
        ('in_repair', 'In Repair'),
        ('repaired', 'Repaired'),
        ('dispatched', 'Dispatched'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    date_of_purchase = models.DateField()
    fault_description = models.TextField()
    photo = models.ImageField(upload_to='uploads/', blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')

    def __str__(self):
        return f"{self.product_name} - {self.serial_number}"    
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question        