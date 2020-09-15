# Generated by Django 3.0.8 on 2020-09-15 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0006_auto_20200913_1831'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='provider',
            options={'verbose_name': 'ספק', 'verbose_name_plural': 'ספקים'},
        ),
        migrations.AlterField(
            model_name='provider',
            name='code',
            field=models.CharField(default='A', max_length=1, verbose_name='קוד'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='providerId',
            field=models.CharField(blank=True, max_length=150, verbose_name='חברה פרטית'),
        ),
    ]