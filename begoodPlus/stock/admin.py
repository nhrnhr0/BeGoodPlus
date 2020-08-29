from django.contrib import admin

from .models import Stock
# Register your models here.
class StockAdmin(admin.ModelAdmin):
    list_display = ('product','catalog_part', 'provider', 'productSize', 'productColor', 'packingType', 'amount',)

    

admin.site.register(Stock, StockAdmin)