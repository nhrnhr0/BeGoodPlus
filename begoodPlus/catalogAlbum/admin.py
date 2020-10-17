from django.contrib import admin

from catalogAlbum.models import CatalogAlbum

from catalogImages.models import CatalogImage

class CatalogImageInline(admin.TabularInline):
    model = CatalogAlbum.images.through
    ordering = ('weight',)
# Register your models here.

from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin
from django.db.models import Count

class CatalogAlbumAdmin(DraggableMPTTAdmin):
    inlines = (CatalogImageInline,)
    list_display = ('tree_actions','indented_title', 'slug', 'get_absolute_url','view_in_website_link','related_images_count',)#'get_absolute_url')
    readonly_fields = ('view_in_website_link','related_images_count',)
    #readonly_fields = ('get_absolute_url',)
    prepopulated_fields = {'slug': ('title',),}
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = qs.annotate(image_count=Count('images'))
        return qs
        
    def related_images_count(self, instance):
        return instance.image_count
    related_images_count.short_description = 'Related images (for this specific album)'


'''
class CatalogAlbumAdmin(admin.ModelAdmin):
    inlines = (CatalogImageInline,)
    list_display = ('__str__', 'slug',)#'get_absolute_url')
    #readonly_fields = ('get_absolute_url',)
    prepopulated_fields = {'slug': ('title',),}
'''
admin.site.register(CatalogAlbum,CatalogAlbumAdmin)