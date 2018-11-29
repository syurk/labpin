from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
#from carton.cart import Cart
#from products.models import Product
#def add(request):
#    cart = Cart(request.session)
#    product = Product.objects.get(id=request.GET.get('product_id'))
#    cart.add(product, price=product.price)
#    return HttpResponse("Added")
#
#def remove(request):
#    cart = Cart(request.session)
#    product = Product.objects.get(id=request.GET.get('product_id'))
#    cart.remove(product, price=product.price)
#    return HttpResponse("Removed")
#
#def shopping(request):
#    context = {}
#    template = 'shopping.html'
#    return render(request,template,context)
#
#
#
#def show(request):
#    return render(request, 'shopping/show-cart.html')