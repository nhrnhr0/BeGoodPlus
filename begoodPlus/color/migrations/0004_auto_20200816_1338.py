# Generated by Django 3.0.8 on 2020-08-16 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('color', '0003_color_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='color name'),
        ),
    ]
