"""begoodPlus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from pages.views import order_form, catalog_view
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from rest_framework import routers
from product.views import ProductViewSet
from category.views import CategoryViewSet
from productImages.views import ProductImageSerializer
from product.views import products_select_all, products_select, product_detail
router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'productImages', ProductImageSerializer)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('order/', order_form),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('order/products_select/<str:phrash>', products_select),
    path('order/products_select/', products_select_all),
    path('order/product_detail/<int:id>', product_detail),
    path('catalog/', catalog_view),
    path('', catalog_view)
]

if settings.DEBUG:
    urlpatterns= urlpatterns + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
    urlpatterns= urlpatterns + static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
