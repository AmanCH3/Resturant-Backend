from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Waiter(models.Model):
    name = models.CharField(max_length=255)
    schedule = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Administrator(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)  # Consider Django's AbstractUser for better password handling

    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255, choices=[('Waiter', 'Waiter'), ('Chef', 'Chef'), ('Manager', 'Manager')])

    def __str__(self):
        return f"{self.name} - {self.position}"
