from django.contrib.gis.db import models


class Adrress(models.Model):
    location = models.PointField()
    state = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    street = models.CharField(max_length=50, null=True, blank=True)
    alley = models.CharField(max_length=50, null=True, blank=True)
    plaque = models.IntegerField(null=True, blank=True)
