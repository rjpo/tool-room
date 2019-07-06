from django.db import models


class Herramienta(models.Model):
    barcode = models.PositiveIntegerField(default=0)
    serial = models.PositiveIntegerField(default=0)
    nombre = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    placa = models.CharField(max_length=9)