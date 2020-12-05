from django.db import models
from Geolocation.models import Adrress


class Store(models.Model):
    name = models.CharField(max_length=50)
    address = models.ForeignKey(Adrress, on_delete=models.RESTRICT)

    def __str__(self):
        if self.address.city :
            return f'{self.id} - {self.name} in {self.address.city} '
        else:
            return f'{self.id} - {self.name} in literaly no where ......'
    
         