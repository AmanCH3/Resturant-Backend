from django.db import models

class Order(models.Model):
    order_number = models.AutoField(primary_key=True)
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ('paid', 'Paid'),
        ('Packed', 'packed'),
        ('Recieved', 'recieved'),
    ]
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="In Progress")
    order_value = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    admin = models.ForeignKey('staff.Administrator', on_delete=models.SET_NULL, null=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey("menus.MenuItem", on_delete=models.CASCADE)
    quantity = models.IntegerField()
