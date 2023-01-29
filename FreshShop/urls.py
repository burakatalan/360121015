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
from django.contrib.auth import views as auth_views
from accounts.views import PasswordsChangeView
from accounts.urls import urlpatterns as accounts_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home, name='shop.home'),
    path("index.html",views.home, name='home'),
    path("index",views.home),
    path("gallery",views.gallery, name='gallery'),
    path("shop/",views.shop, name='shop'),
    #path("shop-detail",views.shopdetail, name='shop-detail'),
    path("cart",views.cart, name='cart'),
    path("wishlist",views.wishlist, name='wishlist'),
    path("accounts",views.myaccount, name='accounts'),
    path("checkout",views.checkout, name='checkout'),
    path("contact-us",views.contactUs, name='contact-us'),
    path("about",views.about, name='about'),
    path("product/<slug:slug>",views.shopdetail, name='product'),
    #path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    #path("register",views.register, name='register'),
    path('accounts/', include('accounts.urls')),
    path('subscribe', views.subscribe, name='subscribe'),
    #path('address', views.address, name='address'),
    path("success/", views.successView, name="success"),
    path("shop/<slug:slug>", views.categoryFilter, name="categoryFilter"),
    #path("payment/", views.payment, name="payment"),
    #path("profile/", PasswordsChangeView.as_view(), name="profile"),
    path("addCart/<int:id>", views.addCart, name="addCart"),
    path("removeCart/<slug:slug>", views.removeCart, name="removeCart"),
    path("product/", views.shop, name="shop"),
    #path(r'^password/$', views.change_password, name='change_password'),
    path("placeOrder/<int:id>", views.placeOrder, name="placeOrder"),
    path("orderPage", views.orderPage,name="orderPage")
    
    
 
]
urlpatterns += static(settings.MEDIA_URL, 
 document_root=settings.MEDIA_ROOT)
