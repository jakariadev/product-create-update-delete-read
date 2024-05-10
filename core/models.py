from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(null=True, blank=True,max_digits=7, decimal_places=2)
    unit = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.name