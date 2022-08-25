from django.contrib import admin

from .models import *
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display =('first_name', 'last_name', 'email', 'address', 'phone', 'date', 'course', 'center', 'mode', 'address')
    list_filter=('first_name', 'last_name', 'date', 'course', 'center', 'mode')


