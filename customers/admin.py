from django.contrib import admin
from .models import Customer 
from orders.models import Cart

# Register your models here.
admin.site.register(Customer)
admin.site.register(Cart)
