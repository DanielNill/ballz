from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    contact_info = models.ForeignKey(ContactInfo)
    photo = models.ImageField(blank=True, null=True)
    stats = models.ForeignKey(Stats)
    
class ContactInfo(models.Model):
    phone = models.CharField(max_length=11, blank=True, null=True)
    email = models.EmailField(blank=True, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=15, blank=True, null=True)
    zipcode = models.IntegerField(blank=True, null=True)
    
class Stat(models.Model):
    stat_type = models.ForeignKey(StatTypes)
    stat_value = models.DoubleField()
    
class StatTypes(models.Model):
    name = models.CharField(max_length=25)        
