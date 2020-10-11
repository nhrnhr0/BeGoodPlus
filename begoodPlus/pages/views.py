from django.shortcuts import render

# Create your views here.


def order_form(request):
    ret = render(request, 'index.html',{})
    return ret
    
def order_form2(request):
    ret = render(request, 'order.html', {})
    return ret
    
def order_form3(request):
    ret = render(request, 'order2.html', {})
    return ret

def catalog_view(request):
    return render(request, 'catalog.html',{})
    
    
def landing_page_view(request):
    return render(request, 'landing_page.html', {})
    
def my_logo_wrapper_view(request):
    return render(request, 'my_logo_wrapper.html', {})

from django.shortcuts import get_object_or_404

def catalog_page(request, *args, **kwargs):
    from catalogAlbum.models import CatalogAlbum
    slug = kwargs['slug']
    album = get_object_or_404(CatalogAlbum.objects.prefetch_related('images'), slug=slug)
    ret = {'album_title': album.title,
            'images': album.images.values().order_by('throughimage__weight'),
    }
    
    return render(request, 'catalog_page.html', {'context':ret})
    