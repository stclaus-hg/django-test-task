from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from django.core.urlresolvers import reverse

from . models import Product, ProductComment


class ProductCommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ('username', 'text')


def index(request):
    return render(request, 'product/index.html', {'products': Product.objects.all()})


def detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        form = ProductCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.save()
            return redirect(reverse('products:detail', args=[product.slug]) )
    else:
        form = ProductCommentForm()
    return render(request, 'product/detail.html',
                  {'product': product,
                   'form': form})
