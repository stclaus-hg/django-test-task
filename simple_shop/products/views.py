from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from . models import Product, ProductComment, ProductLike


class ProductCommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ('username', 'text')


def index(request):
    qs = Product.objects.annotate(likes=Count('productlike'))
    if request.GET.get('sort') == 'likes':
        products = qs.order_by('-likes')
    elif request.GET.get('sort') == 'price':
        products = qs.order_by("price")
    else:
        products = qs.order_by("name")
    return render(request, 'product/index.html', {'products': products})


def detail(request, slug):
    product = get_object_or_404(Product.objects.select_related(), slug=slug)
    if request.method == 'POST':
        form = ProductCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.save()
            return redirect(reverse('products:detail', args=[product.slug]))
    else:
        form = ProductCommentForm()
    return render(request, 'product/detail.html',
                  {'product': product,
                   'form': form})


@login_required
def do_like(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if ProductLike.objects.filter(product=product, user=request.user).count() == 0:
        ProductLike.objects.create(product=product, user=request.user)
    return redirect(reverse('products:detail', args=[product.slug]))
