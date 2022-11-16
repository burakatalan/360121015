"""FreshShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from shop import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home, name='home'),
    path("index.html",views.home, name='home'),
    path("index",views.home),
    path("gallery",views.gallery, name='gallery'),
    path("shop/",views.shop, name='shop'),
    path("shop-detail",views.shopdetail, name='shop-detail'),
    path("cart",views.cart, name='cart'),
    path("wishlist",views.wishlist, name='wishlist'),
    path("my-account",views.myaccount, name='my-account'),
    path("checkout",views.checkout, name='checkout'),
    path("contact-us",views.contactUs, name='contact-us'),
    path("about",views.about, name='about'),
 
]
urlpatterns += static(settings.MEDIA_URL, 
 document_root=settings.MEDIA_ROOT)
