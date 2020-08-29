from django.db import models
from colorfield.fields import ColorField
from django.utils.translation import gettext as _

# Create your models here.
class Color(models.Model):
    name = models.CharField(max_length=30, verbose_name=_('color name'), unique=True)
    color = ColorField(verbose_name=_('color'), default='#FF0000')

    

    def __str__(self):
        return self.name
    