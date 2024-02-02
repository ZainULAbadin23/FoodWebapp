from django.contrib import admin

from .models import Resturant, Product, ProductCategory

# Register your models here.

admin.site.register(Resturant)
admin.site.register(ProductCategory)
admin.site.register(Product)
