from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=220)
    price = models.IntegerField(default=0)
    content = models.TextField(null=True, blank=True)


