from django.db import models

from provider.models import Provider
from productSize.models import ProductSize
from productColor.models import ProductColor
from product.models import Product
from django.utils.translation import gettext as _
from packingType.models import PackingType
# Create your models here.
class Stock(models.Model):
    class Meta():
        verbose_name = _('Stock')
        verbose_name_plural = _('Stocks')
        default_related_name = 'stocks'
        
    product = models.ForeignKey(verbose_name=_("product name"), to=Product, on_delete=models.CASCADE)
    provider = models.ForeignKey(verbose_name=_("product provider"), to=Provider, on_delete=models.CASCADE)
    productSize = models.ForeignKey( verbose_name=_("size"), to=ProductSize, on_delete=models.CASCADE)
    productColor = models.ForeignKey(verbose_name=_("color"), to=ProductColor, on_delete=models.CASCADE)
    packingType = models.ForeignKey(verbose_name=_("packing type"), to=PackingType, on_delete=models.CASCADE)
    providerMakat = models.CharField(verbose_name=_("provider makat"), max_length=50, blank=True)
    amount = models.IntegerField(verbose_name=_('stock at us'), default=0)
    provider_has_stock = models.BooleanField(verbose_name=_("exist at provider"), default=True)
    provider_resupply_date = models.DateTimeField(verbose_name=_("provider resupply date"), null=True, blank=True)

    def catalog_part(self):
        from product.models import Product
        category_rep = self.product.category.catalog_rep
        provider_rep = self.provider.code
        subcat_rep = self.product.catalog_part()
        size_rep = self.productSize.code
        color_rep = self.productColor.code
        product_id = str(self.product.id)
        return category_rep + provider_rep + subcat_rep + '-' + size_rep + '-' + color_rep + '-' + product_id
    catalog_part.short_description = _("makat")
    
    

