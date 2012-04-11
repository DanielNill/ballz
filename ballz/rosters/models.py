from django.contrib.auth.models import User
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

    def __unicode__(self):
        return self.name


class Stat(models.Model):
    stat_type = models.ForeignKey(StatTypes)
    stat_value = models.IntegerField()

    def __unicode__(self):
        return self.state_type

<<<<<<< HEAD

=======
>>>>>>> fbede578d2756c93560071cfd2e44af5010459bc
class Player(models.Model):
    '''
    TODO: change postion so that you can have auto suggest or assign multiple positions to one player
    '''

    name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    contact_info = models.ForeignKey(ContactInfo)
    photo = models.ImageField(upload_to='media/player_photos/', blank=True, null=True)
<<<<<<< HEAD
    stats = models.ForeignKey(Stat, blank=True, null=True)
    created_by = models.ForeignKey(User)

=======
    stats = models.ForeignKey(Stat)
    user = models.ForeignKey(User, default=0) #the user that input that player
>>>>>>> fbede578d2756c93560071cfd2e44af5010459bc
    def __unicode__(self):
        return self.name


class Sport(models.Model):
    name = models.CharField(max_length=100)

<<<<<<< HEAD

=======
>>>>>>> fbede578d2756c93560071cfd2e44af5010459bc
class Team(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    players = models.ManyToManyField(Player)
    sport = models.ForeignKey(Sport)
<<<<<<< HEAD
=======

>>>>>>> fbede578d2756c93560071cfd2e44af5010459bc
