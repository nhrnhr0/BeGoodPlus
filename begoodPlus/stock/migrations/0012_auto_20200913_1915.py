# Generated by Django 3.0.8 on 2020-09-13 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0011_auto_20200913_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='provider_resupply_date',
            field=models.DateTimeField(verbose_name='provider resupply date'),
        ),
    ]
