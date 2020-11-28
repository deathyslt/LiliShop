from django.db import models
from Geolocation.models import Adrress


class Store(models.Model):
    name = models.CharField(max_length=50)
    address = models.ForeignKey(Adrress, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.id} - {self.name}'
