from django.db import models

# Create your models here.
class Table(models.Model):
    table_number = models.IntegerField(unique=True , default=1)
    capacity = models.IntegerField()
    location = models.CharField(max_length=255, choices=
        [('inside', 'Inside'),
        ('outside', 'Outside'),
        ('Terrace', 'Terrace')],
        default='inside'
    )

    availability_status = models.CharField(
        max_length=50,
        choices=[('available', 'Available'), ('occupied', 'Occupied'), ('reserved', 'Reserved')],
        default='available'
    )

    def __str__(self):
        return f"Table for {self.capacity} - {self.availability_status}"
class Reservation(models.Model):
    customer = models.ForeignKey('customers.Customer', on_delete = models.CASCADE)
    # for the different , branch of the restaurant
    table = models.ForeignKey(Table, on_delete = models.CASCADE)
    reservation_date = models.DateTimeField(auto_now_add = True)
    reservation_time = models.TimeField()
