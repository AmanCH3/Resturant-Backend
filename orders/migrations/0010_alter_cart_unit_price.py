# Generated by Django 5.1.1 on 2024-11-18 06:30

import menus.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_rename_cart_id_cart_order_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name=menus.models.Menu),
        ),
    ]
