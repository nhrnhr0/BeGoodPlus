# Generated by Django 3.0.8 on 2020-10-13 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogAlbum', '0004_auto_20201013_0938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalogalbum',
            name='parent',
        ),
    ]