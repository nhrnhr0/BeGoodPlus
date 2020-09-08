# Generated by Django 3.0.8 on 2020-09-08 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submit_date', models.DateField(auto_now=True, verbose_name='submit date')),
                ('client_name', models.CharField(max_length=50, verbose_name='client name')),
                ('private_compeny', models.CharField(max_length=50, verbose_name='חברה פרטית')),
                ('addres', models.CharField(max_length=100, verbose_name='addres')),
                ('telephone', models.CharField(max_length=20, verbose_name='telephone')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('contact_man', models.CharField(max_length=50, verbose_name='contact man')),
                ('cellphone', models.CharField(max_length=20, verbose_name='cellphone')),
            ],
            options={
                'verbose_name': 'מיון',
                'verbose_name_plural': 'Orders',
            },
        ),
    ]
