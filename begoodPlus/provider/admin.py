from django.contrib import admin
from .models import Provider
# Register your models here.
'''from product.models import Product
class productInline(admin.TabularInline):
    #fields = ('render_image',)
    model = Provider.through
    fields = ('image', 'render_image',)
    readonly_fields = ('render_image',)
class castumProviderAdmin(admin.ModelAdmin):
    inlines = [productInline,]

admin.site.register(Provider, castumProviderAdmin)'''

from stock.models import Stock
class StockInline(admin.TabularInline):
    model = Stock
    
    pass
    
class ProviderAdmin(admin.ModelAdmin):
    list_display = ['name', 'stocks_count',]
    inlines = [StockInline,]
    pass
admin.site.register(Provider, ProviderAdmin)