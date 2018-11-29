# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Product, ProductImage


# Create your views here.
def all(request):
    product = Product.objects.all()
    #image = Product.image
    images = ProductImage.objects.all()
    context = {"product": product,"images": images }

    template = 'all.html'
    return render(request,template,context)

#def specific(request, category):
#    cat = Product.objects.get(category=category)
#    images = ProductImage.objects.filter(product=cat)
#
#    context = {"cat": cat,"images": images }
#    template = 'specific.html'
#
#    return render(request,template,context)

def single(request, slug):
    product = Product.objects.get(slug=slug)
	#images = product.productimage_set.all()
    images = ProductImage.objects.filter(product=product)
    context = {'product': product, "images": images}
    template = 'single.html'	
    return render(request, template, context)

