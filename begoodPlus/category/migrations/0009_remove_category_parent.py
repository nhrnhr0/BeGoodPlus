# Generated by Django 3.0.8 on 2020-09-06 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0008_auto_20200906_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
    ]
