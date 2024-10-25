from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    address = models.TextField()
    memebership_status = models.CharField(max_length = 50)
   