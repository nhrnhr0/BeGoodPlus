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