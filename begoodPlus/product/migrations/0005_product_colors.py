# Generated by Django 3.0.8 on 2020-08-04 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productColor', '0002_remove_productcolor_product'),
        ('product', '0004_product_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='colors',
            field=models.ManyToManyField(to='productColor.ProductColor'),
        ),
    ]
