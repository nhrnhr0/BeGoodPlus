# Generated by Django 3.0.8 on 2020-08-02 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('color', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='color',
            name='name',
        ),
    ]
