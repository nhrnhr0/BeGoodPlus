from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class ProductSize(models.Model):

    class Meta():
        verbose_name = _('Product size')
        verbose_name_plural = _('Product sizes')
        
    size = models.CharField(_('size'), default='X', max_length=30, unique=True)
    code = models.CharField(_('code'), default=0, max_length=2)

    def __str__(self):
        return self.size

