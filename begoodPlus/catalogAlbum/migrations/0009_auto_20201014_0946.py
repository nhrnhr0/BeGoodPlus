# Generated by Django 3.0.8 on 2020-10-14 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogAlbum', '0008_auto_20201014_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='throughimage',
            name='weight',
            field=models.IntegerField(verbose_name='משקל'),
        ),
        migrations.AlterUniqueTogether(
            name='throughimage',
            unique_together={('catalogAlbum', 'weight')},
        ),
    ]
