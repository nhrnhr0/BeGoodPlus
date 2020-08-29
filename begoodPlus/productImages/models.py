from django.db import models
from product.models import Product
from django.utils.translation import gettext as _

# Create your models here.
class ProductImage(models.Model):
    image = models.ImageField(verbose_name=_('image'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    @property
    def get_absolute_image_url(self):
        return '%s%s' % (MEDIA_URL, self.image.url)

