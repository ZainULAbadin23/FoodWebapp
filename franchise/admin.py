from django.contrib import admin

from .models import Deliverer, Franchise, Order, Cart

# Register your models here.


admin.site.register(Deliverer)
admin.site.register(Franchise)
admin.site.register(Order)
admin.site.register(Cart)
