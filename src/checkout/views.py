# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required

from django.shortcuts import render

from tryTen import settings

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY
from products.models import Product

# Create your views here.

@login_required
def charge(request):
    
    #if request.method == "POST":
    token    = request.POST.get("stripeToken")

    try:
        charge  = stripe.Charge.create(
            amount      = 2000,
            currency    = "usd",
            source      = token,
            description = "The product charged to the user"
        )


    except stripe.error.CardError as ce:
        return False, ce

    #else:
        
       # return redirect("home")

@login_required
def checkout(request, slug):
    product = Product.objects.get(slug=slug)
    #images = ProductImage.objects.filter(product=product)
    
    #, "images": images
    context = {'product': product, 'stripe_key': settings.STRIPE_PUBLIC_KEY}
    template = 'checkout.html'
    return render(request,template,context)
 
#@login_required
#def charge(request):
#    context = {"stripe_key": settings.STRIPE_PUBLIC_KEY}
#
#    stripe.api_key = settings.STRIPE_SECRET_KEY
#
#    # Token is created using Stripe.js or Checkout!
#    # Get the payment token submitted by the form:
#    token = request.form['stripeToken'] # Using Flask
#
#    # Charge the user's card:
#    charge = stripe.Charge.create(
#      amount=1000,
#      currency="usd",
#      description="Example charge",
#      source=token,
#    )
#
#    template = 'checkout.html'
#    return render(request,template,context)
