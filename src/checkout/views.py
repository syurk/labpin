# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required

from django.shortcuts import render

from tryTen import settings

import stripe

from products.models import Product

# Create your views here.
@login_required
def checkout(request, slug):
    product = Product.objects.get(slug=slug)
    #images = ProductImage.objects.filter(product=product)
    
    #, "images": images
    context = {'product': product}
    template = 'checkout.html'
    return render(request,template,context)

@login_required
def charge(request):
    context = {"stripe_key": settings.STRIPE_PUBLIC_KEY}

    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Token is created using Stripe.js or Checkout!
    # Get the payment token submitted by the form:
    token = request.form['stripeToken'] # Using Flask

    # Charge the user's card:
    charge = stripe.Charge.create(
      amount=1000,
      currency="usd",
      description="Example charge",
      source=token,
    )

    template = 'checkout.html'
    return render(request,template,context)
