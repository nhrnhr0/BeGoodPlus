# Generated by Django 3.0.8 on 2020-11-12 12:51

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='שם צבע')),
                ('color', colorfield.fields.ColorField(default='#FF0000', max_length=18, verbose_name='צבע')),
            ],
            options={
                'verbose_name': 'צבע',
                'verbose_name_plural': 'צבעים',
            },
        ),
    ]
