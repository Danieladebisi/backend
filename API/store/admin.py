from django.contrib import admin

# Register your models here.


from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display=('name', 'description','price','date','image')
    list_filter=('date','name', 'price')


admin.site.register(Product, ProductAdmin)


