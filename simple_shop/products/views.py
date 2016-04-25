from django.shortcuts import render, get_object_or_404
from . models import Product


def index(request):
    return render(request, 'product/index.html', {'products': Product.objects.all()})


def detail(request, slug):
    return render(request, 'product/detail.html', {'product': get_object_or_404(Product, slug=slug)})
