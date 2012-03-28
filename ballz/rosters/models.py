from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length=100)
    
