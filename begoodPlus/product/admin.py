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
    
    show_change_link = True

    def render_image(self, obj):
        ret = ''
        ret += '<img src="%s" width="150" height="150" />' % (settings.MEDIA_URL + obj.image.name) 
        return mark_safe(ret)

from stock.models import Stock
class stockInline(admin.TabularInline):
    model = Stock
    extra = 1
    
    show_change_link = True



class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'category','customer_catalog_gen', 'inst_client_range', 'sing_client_range','render_image',)
    readonly_fields = ('id','category_index','customer_catalog_gen',)
    fieldsets = (
        (None, {
            "fields": (
                ('id','category_index'), 
                'customer_catalog_gen',
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
    
    search_fields = ('name', 'category__title',)
    def get_search_results(self, request, queryset, search_term):
        new_queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        # adding to the original search. search by "customer_catalog_gen"
        for p in queryset:
            if search_term in p.customer_catalog_gen() and p not in new_queryset:
                new_queryset |= Product.objects.filter(pk=p.pk)
        return new_queryset, use_distinct

admin.site.register(Product,ProductAdmin)