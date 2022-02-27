# Generated by Django 4.0.1 on 2022-01-18 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0002_apartment_bed_apartment_double_bed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='cleaning_price',
            field=models.DecimalField(decimal_places=2, default=50, max_digits=9, verbose_name='Общая цена'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='price_per_night',
            field=models.DecimalField(decimal_places=2, default=60, max_digits=9, verbose_name='Общая цена'),
        ),
    ]