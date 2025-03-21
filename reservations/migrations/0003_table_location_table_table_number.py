# Generated by Django 5.1.1 on 2024-11-18 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_table_alter_reservation_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='location',
            field=models.CharField(choices=[('inside', 'Inside'), ('outside', 'Outside'), ('Terrace', 'Terrace')], default='inside', max_length=255),
        ),
        migrations.AddField(
            model_name='table',
            name='table_number',
            field=models.IntegerField(default=1, unique=True),
        ),
    ]
