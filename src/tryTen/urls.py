"""tryTen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from checkout import views as checkout_views
from contact import views as contact_views
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from products import views as product_views
from profiles import views as profile_views
from shopping import urls
from shopping import views as shopping_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', profile_views.home, name='home'),
    url(r'^about/$', profile_views.about, name='about'),
    url(r'^profile/$', profile_views.userProfile, name='profile'),
    url(r'^products/$', product_views.all, name='products'),
    url(r'^product/(?P<slug>[\w-]+)/$', product_views.single, name='product'),
    #url(r'^product/$', product_views.single, name='product'),
    url(r'^checkout/(?P<slug>[\w-]+)/$', checkout_views.checkout, name='checkout'),
    url(r'^charge/$', checkout_views.checkout, name='charge'),
    url(r'^contact/$', contact_views.contact, name='contact'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^payments/', include('djstripe.urls', namespace="djstripe")),
    #url(r'^shopping-cart/', include('shopping.urls')),
    #url(r'^shopping/$', shopping_views.shopping, name='shopping'),
]#+static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)

#if in the setting files DEBUG is true use this static url
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)