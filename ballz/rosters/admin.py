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

class StatAdmin(admin.ModelAdmin):
    list_display = ['stat_type', 'stat_value']
    
    fieldsets = [
        (None, {'fields':['stat_type', 'stat_value']})
    ]
    
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'position', 'contact_info', 'photo', 'stats']
    
    fieldsets = [
        (None, {'fields':['name', 'age', 'position', 'contact_info', 'photo', 'stats']})
    ]
         
admin.site.register(ContactInfo, ContactInfoAdmin)
admin.site.register(StatTypes, StatTypesAdmin)
admin.site.register(Player, PlayerAdmin)