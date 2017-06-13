from django.db import models


class Category(models.Model):
    name = models.CharField(default='', max_length=50)
    thumbnail = models.URLField(default='')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(default='', max_length=50)
    description = models.TextField(default='')
    model = models.CharField(default='', max_length=50)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        default=1
    )
    thumbnail = models.URLField(default='')

    def __str__(self):
        return self.name


class Photos(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        default=1
    )
    photo_url = models.URLField(default='')
