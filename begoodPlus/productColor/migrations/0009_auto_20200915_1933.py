# Generated by Django 3.0.8 on 2020-09-15 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productColor', '0008_auto_20200913_1831'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcolor',
            options={'ordering': ('code',), 'verbose_name': 'צבע מוצר', 'verbose_name_plural': 'צבעי מוצר'},
        ),
        migrations.AlterField(
            model_name='productcolor',
            name='code',
            field=models.CharField(max_length=2, verbose_name='קוד'),
        ),
    ]
