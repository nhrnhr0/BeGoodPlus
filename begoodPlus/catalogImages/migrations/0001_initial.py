# Generated by Django 3.0.8 on 2020-10-10 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='כותרת')),
                ('description', models.TextField(verbose_name='description')),
                ('image', models.ImageField(upload_to='', verbose_name='תמונה')),
                ('image_thumbnail', models.ImageField(blank=True, null=True, upload_to='', verbose_name='image thumbnail')),
            ],
            options={
                'verbose_name': 'Catalog image',
                'verbose_name_plural': 'Catalog images',
            },
        ),
    ]