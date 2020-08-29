from django.db import models
from category.models import Category
from django.utils.translation import gettext as _
from productColor.models import ProductColor
from provider.models import Provider
from packingType.models import PackingType
from utils.utils import get_next_value
from django.utils.html import mark_safe
from django.conf import settings
from utils import utils
#from sequences import get_next_value
# Create your models here.
class Product(models.Model):
    class Meta():
        ordering = ('category',)
    name = models.CharField(max_length=120, verbose_name=_('name'))
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    #running_code = models.IntegerField(verbose_name='sub-catalog')
    category_index = models.IntegerField()

    #cost_prices = models.IntegerField(verbose_name=_('cost prices'), null=True, default=0)
    const_inst_client_min = models.IntegerField(verbose_name=_('cost for institucional from'),null=True, default=0)
    const_inst_client_max = models.IntegerField(verbose_name=_('to'),null=True, default=0)
    const_sing_client_min = models.IntegerField(verbose_name=_('cost for single client from'),null=True, default=0)
    const_sing_client_max = models.IntegerField(verbose_name=_('to'),null=True, default=0)
    #packing = models.ForeignKey(to=PackingType, on_delete=models.CASCADE, default=0)
    suport_printing = models.BooleanField(verbose_name=_('suport printing'), default=True)
    suport_embroidery = models.BooleanField(verbose_name=_('suport embroidery'), default=True)
    content = models.TextField(verbose_name=_('content'), blank=True, default='')
    comments = models.TextField(verbose_name=_('comments'),blank=True, default='')

    def __str__(self):
        return self.name

    def catalog_part(self, *args, **kwargs):
        return ''.join(utils.catalog_representation[self.category_index])

    def customer_catalog(self, *args, **kwargs):
        ret = self.category.catalog_rep + 'z' + self.catalog_part() + '-' + str(self.id)
        return ret


    def save(self, *args, **kwargs):
        if self.category_index == None:
            self.category_index = self.category.itemsCount + 1
            Category.objects.filter(pk=self.category.pk).update(itemsCount=self.category_index)
        super(Product, self).save(*args, **kwargs)
        pass

    def inst_client_range(self, *args, **kwargs):
        return '(' + str(self.const_inst_client_min) + ' - ' +  str(self.const_inst_client_max) + ')'

    def sing_client_range(self, *args, **kwargs):
        return '(' + str(self.const_sing_client_min) + ' - ' +  str(self.const_sing_client_max) + ')'


    def render_image(self, *args, **kwargs):
        from productImages.models import ProductImage
        images = ProductImage.objects.filter(product=self)
        #print(images.get())
        ret = ''
        for image in images:
            ret += '<img src="%s" width="150" height="150" />' % (settings.MEDIA_URL + image.image.name) 
        return mark_safe(ret)

