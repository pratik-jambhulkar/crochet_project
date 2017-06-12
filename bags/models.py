from django.db import models


class Product(models.Model):
    name = models.CharField(default='', max_length=50)
    description = models.TextField(default='')
    model = models.CharField(default='', max_length=50)
    price = models.IntegerField(default=0)
