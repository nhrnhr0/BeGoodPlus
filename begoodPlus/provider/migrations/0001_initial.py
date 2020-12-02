# Generated by Django 3.0.8 on 2020-11-12 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='שם')),
                ('providerId', models.CharField(blank=True, max_length=150, verbose_name='חברה פרטית')),
                ('code', models.CharField(default='A', max_length=1, verbose_name='קוד')),
            ],
            options={
                'verbose_name': 'ספק',
                'verbose_name_plural': 'ספקים',
                'default_related_name': 'providers',
            },
        ),
    ]
