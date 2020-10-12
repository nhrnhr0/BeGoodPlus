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
        ('color', '0001_initial'),
        ('glofa_types', '0001_initial'),
        ('order_detail', '0001_initial'),
        ('glofa_types', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetailAddons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_print', models.BooleanField(verbose_name='is print')),
                ('image', models.ImageField(upload_to='', verbose_name='logo')),
                ('logoDescription', models.TextField(verbose_name='logo description')),
                ('color', models.ManyToManyField(to='color.Color')),
                ('glofa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='glofa_types.GlofaType', verbose_name='glofa')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_detail.OrderDetail')),
            ],
            options={
                'verbose_name': 'Order detail addons',
                'verbose_name_plural': 'Order detail addons',
            },
        ),
    ]
