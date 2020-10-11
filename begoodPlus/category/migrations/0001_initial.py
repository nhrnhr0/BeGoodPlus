# Generated by Django 3.0.8 on 2020-10-10 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='כותרת')),
                ('itemsCount', models.IntegerField(default=0)),
                ('catalog_rep', models.CharField(blank=True, max_length=1, verbose_name='ייצוג קטלוגי')),
            ],
            options={
                'verbose_name': 'קטגוריה',
                'verbose_name_plural': 'קטגוריות',
                'ordering': ['-title'],
            },
        ),
    ]
