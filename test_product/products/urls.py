from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^/products/$', views.index, name='products'),
    url(r'^/products/')
]