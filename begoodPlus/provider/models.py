from django.db import models
from django.utils.translation import gettext as _
from colorfield.fields import ColorField
# Create your models here.
class Provider(models.Model):

    class Meta():
        verbose_name = _('Provider')
        verbose_name_plural = _('Providers')

    name = models.CharField(max_length=150, verbose_name=_('name'))
    providerId = models.CharField(max_length=150, verbose_name=_('private compeny'), blank=True)
    code = models.CharField(verbose_name=_('code'), max_length=1, default='A')
    #color = models.ForeignKey(Color, on_delete=models.CASCADE)
    #color = ColorField(verbose_name=_('color'))

    def __str__(self):
        return self.name
 
