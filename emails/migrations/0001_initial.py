# Generated by Django 4.0.1 on 2022-01-27 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apartments', '0010_booking_is_accept'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Tipe de email',
            },
        ),
        migrations.CreateModel(
            name='EmailSendingFact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('order', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='apartments.booking')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emails.emailtype')),
            ],
            options={
                'verbose_name': 'Email enviado',
            },
        ),
    ]