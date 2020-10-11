from django.db import models
# Create your models here.
from django.utils.translation import gettext as _

from catalogImages.models import CatalogImage
class CatalogAlbum(models.Model):
    title = models.CharField(max_length=120, verbose_name=_("title"))
    slug = models.SlugField(max_length=120, verbose_name=_("slug"), unique=True)
    images = models.ManyToManyField(to=CatalogImage, related_name='images', null=True, blank=True, through='ThroughImage')# 
    def __str__(self):
        return self.title
    
    def get_absolute_url(self, *args, **kwargs):
        from django.urls import reverse
        return reverse('albumView', args=[self.slug])


class ThroughImage(models.Model):
    catalogImage = models.ForeignKey(CatalogImage, on_delete=models.CASCADE)
    catalogAlbum = models.ForeignKey(CatalogAlbum, on_delete=models.CASCADE)
    weight = models.IntegerField(verbose_name=_("weight"), unique=True)
    
    class Meta:
        ordering = ['weight']

