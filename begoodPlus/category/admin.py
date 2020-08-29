from django.contrib import admin
from .models import Category
# Register your models here.

from product.models import Product
class ProductInline(admin.TabularInline):
    model = Product
    fields = ('name', 'content')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent','catalog_rep',  'itemsCount', '__str__')

    inlines = [ProductInline,]
admin.site.register(Category,CategoryAdmin)