from decimal import Decimal

from datetime import timedelta

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase

# Create your tests here.
from django.utils import timezone
from .models import Product, ProductComment


class ProductDetailTest(TestCase):
    def create_product(self):
        return Product.objects.create(
            name='test product 1',
            slug='test_product_1',
            description='description test_product_1',
            price=Decimal('12.45')
        )

    def test_product_info(self):
        product = self.create_product()
        response = self.client.get(reverse('products:detail', args=[product.slug]))
        self.assertContains(response, product.name, status_code=200)
        self.assertContains(response, product.description, status_code=200)
        self.assertContains(response, product.price, status_code=200)

    def test_show_like_link(self):
        product = self.create_product()
        user = User.objects.create_user('admin', 'admin@example.com', '1qazxsw2')

        response = self.client.get(reverse('products:detail', args=[product.slug]))
        self.assertNotContains(response,
                               '<a href="%s">Like</a>' % reverse('products:detail', args=[product.slug]),
                               status_code=200)

        login_result = self.client.login(username=user.username, password='1qazxsw2')
        self.assertTrue(login_result)

        response = self.client.get(reverse('products:detail', args=[product.slug]))
        self.assertContains(response,
                            '<a href="%s">Like</a>' % reverse('products:like', args=[product.slug]),
                            status_code=200)

    def test_add_like(self):
        product = self.create_product()
        user = User.objects.create_user('admin', 'admin@example.com', '1qazxsw2')

        login_result = self.client.login(username=user.username, password='1qazxsw2')
        self.assertTrue(login_result)

        response = self.client.post(reverse('products:like', args=[product.slug]), follow=True)
        self.assertContains(response, 'Likes: 1', status_code=200)

    def test_add_comment(self):
        comment = {'username': 'test_user', 'text': 'Test comment'}
        product = self.create_product()
        response = self.client.post(
            reverse('products:detail', args=[product.slug]),
            comment,
            follow=True
        )
        self.assertContains(response, comment['username'], status_code=200)
        self.assertContains(response, comment['text'], status_code=200)

    def test_show_comments(self):
        comment = {'username': 'test_user', 'text': 'Test comment'}
        product = self.create_product()
        for i in range(10):
            product.productcomment_set.create(
                username='%s_%s' % (comment['username'], i),
                text='%s of user: %s_%s' % (comment['text'], comment['username'], i)
            )

        response = self.client.get(reverse('products:detail', args=[product.slug]))
        for i in range(10):
            self.assertContains(response, '%s_%s' % (comment['username'], i))
            self.assertContains(response, '%s of user: %s_%s' % (comment['text'], comment['username'], i))



