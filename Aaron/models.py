from django.db import models
from Store.models import Store


class Flower(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50, default='fuchsia')
    price = models.IntegerField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.color}'
