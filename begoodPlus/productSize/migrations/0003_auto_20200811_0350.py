# Generated by Django 3.0.8 on 2020-08-11 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productSize', '0002_productsize_size6xl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsize',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productsize',
            name='size32',
        ),
        migrations.RemoveField(
            model_name='productsize',
            name='size33',
        ),
        migrations.RemoveField(
            model_name='productsize',
            name='size34',
        ),
        migrations.RemoveField(
            model_name='productsize',
            name='size35',
        ),
        migrations.RemoveField(
            model_name='productsize',
            name='size36',
        ),
        migrations.RemoveField(
            model_name='productsize',
            name='size37',
        ),
        migrations.RemoveField(
            model_name='productsize',
            name='size38',
        ),
        migrations.RemoveField(
            model_name='productsize',
            name='size39',
        ),
        migrations.RemoveField(
            model_name='productsize',
            name='size3XL',
        ),
        migrations.RemoveField(
            model_name='productsize',
            name='size40',
        ),
        migrations.RemoveField(
            model_name='productsize',
            name='size41',
        ),
        migrations.RemoveField(
            model_name='productsize',
            name='size42',
        ),
        migrations.RemoveField(
            model_name='productsize',
            name='size43',
        ),
        migrations.RemoveField(
            model_name='productsize',
            name='size44',
        ),
        migrations.RemoveField(
            model_name='productsize',
            name='size45',
        ),
        migrations.RemoveField(
            model_name='productsize',
            name='size46',
        ),
        migrations.RemoveField(
            model_name='productsize',
            name='size47',
        ),
        migrations.RemoveField(
            model_name='productsize',
            name='size4XL',
        ),
        migrations.RemoveField(
            model_name='productsize',
            name='size5XL',
        ),
        migrations.RemoveField(
            model_name='productsize',
            name='size6XL',
        ),
        migrations.RemoveField(
            model_name='productsize',
            name='sizeL',
        ),
        migrations.RemoveField(
            model_name='productsize',
            name='sizeM',
        ),
        migrations.RemoveField(
            model_name='productsize',
            name='sizeS',
        ),
        migrations.RemoveField(
            model_name='productsize',
            name='sizeXL',
        ),
        migrations.RemoveField(
            model_name='productsize',
            name='sizeXXL',
        ),
        migrations.AddField(
            model_name='productsize',
            name='code',
            field=models.CharField(default=0, max_length=2, unique=True, verbose_name='code'),
        ),
        migrations.AddField(
            model_name='productsize',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productsize',
            name='size',
            field=models.CharField(default='X', max_length=30, verbose_name='size'),
        ),
    ]
