from django.shortcuts import render

# Create your views here.


def order_form(request):
    ret = render(request, 'index.html',{})
    print("done")
    return ret

def catalog_view(request):
    return render(request, 'catalog.html',{})