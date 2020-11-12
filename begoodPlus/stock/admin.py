from django.contrib import admin

from .models import Stock
# Register your models here.
class StockAdmin(admin.ModelAdmin):
    list_display = ('product','catalog_part', 'provider', 'productSize', 'productColor', 'packingType', 'amount','provider_has_stock','provider_resupply_date')
    list_filter = ('provider','product', 'productSize', 'productColor', 'packingType','provider_has_stock','provider_resupply_date')
    

admin.site.register(Stock, StockAdmin)