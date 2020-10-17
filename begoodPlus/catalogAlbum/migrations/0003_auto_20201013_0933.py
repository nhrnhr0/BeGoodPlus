# Generated by Django 3.0.8 on 2020-10-13 06:33

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalogAlbum', '0002_catalogalbum_relatedalbums'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalogalbum',
            name='relatedAlbums',
        ),
        migrations.AddField(
            model_name='catalogalbum',
            name='level',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='catalogalbum',
            name='lft',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='catalogalbum',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='catalogAlbum.CatalogAlbum'),
        ),
        migrations.AddField(
            model_name='catalogalbum',
            name='rght',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='catalogalbum',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
            preserve_default=False,
        ),
    ]