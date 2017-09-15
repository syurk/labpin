# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import stripe

# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(default='description default text')
    #location = models.CharField(max_length=120, default ='my location default', blank=True, null =True)
    #job = models.CharField(max_length=120, null = True)

    #def charge(self, request, email, fee):
    #    # Set your secret key: remember to change this to your live secret key
    ## in production. See your keys here https://manage.stripe.com/account
    #stripe.api_key = settings.STRIPE_SECRET_KEY
    ## Get the credit card details submitted by the form
    #token = request.POST['stripeToken']


    # Create a Customer
    #stripe_customer = stripe.Customer.create(
    #    card=token,
    #    description=email
    #)

    ## Save the Stripe ID to the customer's profile
    #self.stripe_id = stripe_customer.id
    #self.save()
    ## Charge the Customer instead of the card
    #stripe.Charge.create(
    #    amount=fee, # in cents
    #    currency="usd",
    #    customer=stripe_customer.id
    #)


    def __unicode__(self):
        return self.name