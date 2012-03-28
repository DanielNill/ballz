from django.db import models

class Field(models.Model):
    name = models.CharField(max_length=65)
    location = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Reservation(models.Model):
    field = models.ForeignKey(Field)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __unicode__(self):
        return 'reservation ' + self.id
