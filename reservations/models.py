from django.db import models

# Create your models here.
class Reservation(models.Model):
    customer = models.ForeignKey('customers.Customer', on_delete = models.CASCADE)
    table = models.ForeignKey('tables.Table', on_delete = models.CASCADE)
    admin = models.ForeignKey('staff.Administrator', on_delete = models.SET_NULL, null=True)
    reservation_date = models.DateTimeField(auto_now_add = True)
    reservation_time = models.TimeField()