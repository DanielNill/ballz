from django.db import models

class ContactInfo(models.Model):
    phone = models.CharField(max_length=11, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=15, blank=True, null=True)
    zipcode = models.IntegerField(blank=True, null=True)
    
    def __unicode__(self):
        return self.phone

class StatTypes(models.Model):
    name = models.CharField(max_length=25)

class Stat(models.Model):
    stat_type = models.ForeignKey(StatTypes)
    stat_value = models.IntegerField()
    
class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    contact_info = models.ForeignKey(ContactInfo)
    photo = models.ImageField(upload_to='media/player_photos/', blank=True, null=True)
    stats = models.ForeignKey(Stat)

    def __unicode__(self):
        return self.name