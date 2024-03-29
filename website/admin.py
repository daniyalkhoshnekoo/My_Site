from django.contrib import admin
from .models import *

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('subject','name','email','created_date')
    list_filter = ('email',)
    search_fields = ('name','message')

admin.site.register(Contact, ContactAdmin)