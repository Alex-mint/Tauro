# Generated by Django 4.0.1 on 2022-02-03 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0003_emailtype_subject_alter_emailtype_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailsendingfact',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='emails.emailtype'),
        ),
    ]
