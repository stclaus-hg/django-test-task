from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=20, unique=True, db_index=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
