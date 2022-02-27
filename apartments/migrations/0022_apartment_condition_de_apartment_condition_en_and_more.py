# Generated by Django 4.0.1 on 2022-02-06 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0021_alter_category_options_alter_pageinfo_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='condition_de',
            field=models.TextField(blank=True, null=True, verbose_name='Condiciones'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='condition_en',
            field=models.TextField(blank=True, null=True, verbose_name='Condiciones'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='condition_es',
            field=models.TextField(blank=True, null=True, verbose_name='Condiciones'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='description_long_de',
            field=models.TextField(default='sin descripción', null=True, verbose_name='Descripción larga'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='description_long_en',
            field=models.TextField(default='sin descripción', null=True, verbose_name='Descripción larga'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='description_long_es',
            field=models.TextField(default='sin descripción', null=True, verbose_name='Descripción larga'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='description_short_de',
            field=models.TextField(default='sin descripción', null=True, verbose_name='Descripción corta'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='description_short_en',
            field=models.TextField(default='sin descripción', null=True, verbose_name='Descripción corta'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='description_short_es',
            field=models.TextField(default='sin descripción', null=True, verbose_name='Descripción corta'),
        ),
        migrations.AddField(
            model_name='extras',
            name='extra_de',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Extra'),
        ),
        migrations.AddField(
            model_name='extras',
            name='extra_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Extra'),
        ),
        migrations.AddField(
            model_name='extras',
            name='extra_es',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Extra'),
        ),
        migrations.AddField(
            model_name='pageinfo',
            name='info_de',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='pageinfo',
            name='info_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='pageinfo',
            name='info_es',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='pageinfo',
            name='title_de',
            field=models.CharField(default='info', max_length=255, null=True, verbose_name='Nombtre'),
        ),
        migrations.AddField(
            model_name='pageinfo',
            name='title_en',
            field=models.CharField(default='info', max_length=255, null=True, verbose_name='Nombtre'),
        ),
        migrations.AddField(
            model_name='pageinfo',
            name='title_es',
            field=models.CharField(default='info', max_length=255, null=True, verbose_name='Nombtre'),
        ),
    ]