from django.contrib import admin
from unicodedata import category

from .Products import Product
from .category import Category

class Productinfo(admin.ModelAdmin):
    list_display = ["name","category","price"]
admin.site.register(Product,Productinfo)
admin.site.register(Category)
