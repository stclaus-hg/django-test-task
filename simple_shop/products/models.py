from __future__ import unicode_literals

from datetime import timedelta

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

@python_2_unicode_compatible
class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=20, unique=True, db_index=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('products:detail', args=[self.slug])

    def last_comments(self):
        period_limit = timezone.now()-timedelta(hours=24)
        return self.productcomment_set.filter(created_at__gte=period_limit).order_by("-created_at")


@python_2_unicode_compatible
class ProductComment(models.Model):
    product = models.ForeignKey(Product)
    username = models.CharField(max_length=30, verbose_name='Your name')
    text = models.TextField(verbose_name='Comment')
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'product_comments'

    def __str__(self):
        return '<%s: %s>' % (self.username, self.test[:30])
