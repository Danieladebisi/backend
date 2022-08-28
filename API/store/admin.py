from django.contrib import admin

# Register your models here.

from .models import *



class ProductAdmin(admin.ModelAdmin):
    list_display=('name',  'price', 'description', 'image', 'date')
    list_filter=('name', 'date', 'price')


admin.site.register(Product, ProductAdmin)