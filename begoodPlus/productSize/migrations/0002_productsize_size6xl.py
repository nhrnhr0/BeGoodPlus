# Generated by Django 3.0.8 on 2020-08-04 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productSize', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsize',
            name='size6XL',
            field=models.BooleanField(default=False, verbose_name='6XL'),
        ),
    ]
