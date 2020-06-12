from django.contrib import admin

# Register your models here.
from .models import Product, Contact, Orders, OrderUpdate,Recharge,Bill

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
admin.site.register(Recharge)
admin.site.register(Bill)
