from django.db import models
from menus.models import Menu
from customers.models import Customer
from django.utils import timezone

class Cart(models.Model):
    order_number = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    unit_price = models.DecimalField(Menu, decimal_places=2, max_digits=10 , default=0.00 , null=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    shipping_address = models.TextField(null=True, blank=True)
    special_instructions = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Calculate the total price automatically
        self.total_price = (self.unit_price * self.quantity) - self.discount
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.item_name}"

class Checkout(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ('Received', 'Received'),
        ('Scheduled', 'Scheduled'), 
        ('Shipped', 'Shipped'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="In Progress")
    order_date = models.DateTimeField(default=timezone.now)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    expected_delivery_date = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # fetching the price as foreign key from the menu model
        if self.Menu :
            self.unit_price = self.Menu.price
            self.item_name = self.Menu.item_name
            

      
        # Copy total_price from the associated Cart instance
        self.total_price = self.cart.total_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.cart.cart_id} - {self.cart.customer.username}"