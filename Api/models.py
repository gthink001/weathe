from django.db import models
from jsonfield import JSONField

class Scheduling(models.Model):
    Devicename = models.CharField(max_length=67)
    temp = models.CharField(max_length=254)
    hum = models.CharField(max_length=254)
    ppm = models.CharField(max_length=254)
    bat = models.CharField(max_length=254)
    sol = models.CharField(max_length=254)
    Timestamp = models.DateTimeField(blank=True, null=True)
    objects = models.Manager()

