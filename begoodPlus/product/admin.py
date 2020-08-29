from django.contrib import admin
from .models import Product

from productImages.models import ProductImage
from django.utils.html import mark_safe
from django.conf import settings
class productImageInline(admin.TabularInline):
    #fields = ('render_image',)
    model = ProductImage
    fields = ('image', 'render_image',)
    readonly_fields = ('render_image',)

    extra = 2

    def render_image(self, obj):
        ret = ''
        ret += '<img src="%s" width="150" height="150" />' % (settings.MEDIA_URL + obj.image.name) 
        return mark_safe(ret)

from stock.models import Stock
class stockInline(admin.TabularInline):
    model = Stock
    extra = 1



class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'category','customer_catalog', 'catalog_part', 'inst_client_range', 'sing_client_range', 'category_index','render_image',)
    readonly_fields = ('id','category_index',)
    fieldsets = (
        (None, {
            "fields": (
                ('id','category_index'), 
                'name', 'category',
                ('const_inst_client_min', 'const_inst_client_max'),
                ('const_sing_client_min', 'const_sing_client_max'),
                ('suport_printing', 'suport_embroidery'),
                'content','comments',
            ),
        }),
    )
    #exclude = ('category_index',)
    inlines = [productImageInline,stockInline] # productColorInline

admin.site.register(Product,ProductAdmin)