from django.db import models
from django.urls import reverse


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=256)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    def return_link(self):
        return reverse('item', args=[self.pk])