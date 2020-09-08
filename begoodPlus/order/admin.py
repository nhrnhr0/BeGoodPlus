from django.contrib import admin
from order.models import Order
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('submit_date', 'client_name', 'private_compeny', 'addres', 'telephone', 'email', 'contact_man', 'cellphone',)


admin.site.register(Order,OrderAdmin)