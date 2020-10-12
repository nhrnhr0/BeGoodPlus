<<<<<<< Updated upstream
# Generated by Django 3.0.8 on 2020-10-11 02:22
=======
# Generated by Django 3.0.8 on 2020-10-11 02:07
>>>>>>> Stashed changes

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='תמונה')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.Product', verbose_name='מוצר')),
            ],
            options={
                'verbose_name': 'תמונת מוצר',
                'verbose_name_plural': 'תמונות מוצרים',
                'default_related_name': 'images',
            },
        ),
    ]
