# Generated by Django 4.1.7 on 2023-03-20 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarsApp', '0002_vehiculos_delete_americano'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculos',
            name='valor_vehiuclo_usd',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
