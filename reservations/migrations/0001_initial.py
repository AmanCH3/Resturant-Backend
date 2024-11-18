# Generated by Django 5.1.1 on 2024-11-13 06:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_date', models.DateTimeField(auto_now_add=True)),
                ('reservation_time', models.TimeField()),
                ('admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='staff.administrator')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.table')),
            ],
        ),
    ]
