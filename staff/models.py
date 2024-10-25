from django.db import models

# Create your models here.
class Waiter(models.Model):
    name = models.CharField(max_length = 255)
    schedule = models.CharField(max_length = 255)


class Table(models.Model):
    capacity = models.IntegerField()
    availability_status = models.CharField(max_length = 50)



class Administrator(models.Model):
    name = models.CharField(max_length = 255)
    username = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)