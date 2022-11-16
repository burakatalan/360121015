from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Cart

# Create your views here.

def home(request):
    return render(request, "home.html")

def gallery(request):
    return render(request, 'gallery.html')

def shop(request):
    return render(request, 'shop.html')

def shopdetail(request):
    return render(request, 'shop-detail.html')
    
def cart(request):
    return render(request, 'cart.html')
    
def wishlist(request):
    return render(request, 'wishlist.html')
    
def myaccount(request):
    return render(request, 'my-account.html')
    
def about(request):
    return render(request, 'about.html')

def checkout(request):
    return render(request, 'checkout.html')   
  
def contactUs(request):
    return render(request, 'contact-us.html')      
    

   
def Cart(request):
 searchTerm = request.GET.get('searchItems')
 products = Cart.objects.all()
 return render(request, 'cart.html',
 {'searchTerm':searchTerm, 'products': products})
    
    