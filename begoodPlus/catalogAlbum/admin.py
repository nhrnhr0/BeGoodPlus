from django.contrib import admin

from catalogAlbum.models import CatalogAlbum

from catalogImages.models import CatalogImage
class CatalogImageInline(admin.TabularInline):
    model = CatalogAlbum.images.through
    ordering = ('weight',)
# Register your models here.
class CatalogAlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'get_absolute_url')
    prepopulated_fields = {'slug': ('title',)}
    #autocomplete_fields = ('images',)
    inlines = (CatalogImageInline, )
    

admin.site.register(CatalogAlbum,CatalogAlbumAdmin)