# Generated by Django 3.0.8 on 2020-09-13 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='private_compeny',
            field=models.CharField(max_length=50, verbose_name='private compeny'),
        ),
    ]
