from django.conf import settings
from django.db import models


class Product(models.Model):
    "Generated Model"
    name = models.TextField()
    price = models.DecimalField(
        max_digits=30,
        decimal_places=10,
    )
