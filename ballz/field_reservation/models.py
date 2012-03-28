from django.db import models

# Create your models here.
class Field(models.Model):
    name = models.CharField(max_length=65)
    location = model
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
