from django.contrib import admin
from django import forms
from rosters.models import *

class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['phone', 'email', 'address', 'city', 'state']
    search_fields = []
    list_select_related = True
    
    fieldsets = [
        (None, {'fields': ['phone', 'email', 'address', 'city', 'state', 'zipcode', ]})
    ]

class StatTypesAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_field = []
    list_select_related = True
    
    fieldsets = [
        (None, {'fields':['name']})]  
         
admin.site.register(ContactInfo, ContactInfoAdmin)
admin.site.register(StatTypes, StatTypesAdmin)