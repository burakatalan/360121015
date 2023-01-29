from django.shortcuts import render, redirect
from django.contrib.messages import success
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Cart, Category, Newsteller,Product, ShoppingSession,UserInf,UserAdress,UserPayment,Orders,OrderItems
from .forms import ContactForm,PersonForm,PasswordChangeForm, QtyForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .filters import ProductFilter
from django.contrib.auth.models import User

 #CardForm


# Create your views here.

def home(request):
    
    productFilter = ProductFilter(request.GET, queryset=Product.objects.all())
    context ={
        'Categories': Category.objects.all(),
        'products': productFilter,
        }
   
    return render(request, "home.html",context)

def gallery(request):
    return render(request, 'gallery.html')

def shop(request):
    context ={
        'Products': Product.objects.all(),
        'Categories': Category.objects.all(), 
    }
    return render(request, 'shop.html', context,)
@login_required
def wishlist(request):
    return render(request, 'wishlist.html')
@login_required    
def myaccount(request):
    return render(request, 'my-account.html')
    
def about(request):
    return render(request, 'about.html')

def checkout(request):
    objects = Cart.objects.filter(user_id=request.user,ordered=False)
    session = ShoppingSession.objects.get(user_id=request.user)
    address = UserAdress.objects.get(user_id=request.user)
    payment = UserPayment.objects.get(user_id = request.user)
    for item in objects:
        total = item.product_id.price * item.quantity
    total = session.total
    totals = total*18/100
    subTotal = total - totals
    tax= total*18/100
    context = {
        # 'card_title':payment.title,
        # 'card_no':payment.card_no,
        # 'expiration':payment.expiration,
        # 'cvv':payment.cvv,
        # 'name':payment.name,
        'payment':payment,
        'objects': objects,
        'total': total,
        'quantity': item.quantity,
        'address': address,
        'total': total,
        'subTotal':subTotal,
        'tax':tax,
        
    }
    return render(request, 'checkout.html',context)


    return render(request, 'checkout.html')   

def contactUs(request):
    context ={}
    url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            
            return HttpResponseRedirect(url)
    
    else:
        context['form'] = ContactForm()


    return render(request, 'contact-us.html',context)   
@login_required
def address(request):
    return render(request, 'address.html')  

def subscribe(request):
   if request.method == 'POST':
    email = request.POST.get('email', None)
    subscribe_model_instance = Newsteller()
    subscribe_model_instance.email = email
    subscribe_model_instance.save()
    success(request, f'{email} email was successfully subscribed to our newsletter!')
    return redirect(request.META.get("HTTP_REFERER", "/"))
   



def successView(request):
    return HttpResponse("Success! Thank you for your message.")
    
def categoryFilter(request,slug):
   productFilter = ProductFilter(request.GET, queryset=Product.objects.all())
   context ={
        'Products': Product.objects.filter(category_id__slug=slug),
        'Count': Product.objects.filter(category_id__slug=slug).count(),
        'Categories': Category.objects.all(),
        'slugs': Category.objects.filter(slug=slug),
        'productFilter': productFilter,
      
        }
   return render(request, 'shop.html', context)


def shopdetail(request,slug):
    form = QtyForm(request.POST)
    context ={
        'form' : form,
        'product': Product.objects.get(slug=slug),
        'sliderproducts': Product.objects.all(),
    }
    
    return render(request, 'shop-detail.html',context)

@login_required
def cart(request):

    session = ShoppingSession.objects.get(user_id=request.user)
    
   
    objects = Cart.objects.filter(user_id=request.user,ordered=False)
    total = session.total
    subTotal = total - (total*18/100)
    tax= total*18/100
    for Product in objects:
        pass
      #  prdTotal = Product.price * Product.quantity
    context = {
        'objects': objects,
        'total': total,
        'subTotal':subTotal,
        'tax':tax,
       # 'prdTotal': prdTotal,
    }
    return render(request, 'cart.html',context)



@login_required
def addCart(request,id):
    url = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=id)
    price = product.price
    session, created = ShoppingSession.objects.get_or_create(user_id=request.user)
    priceTotal = ShoppingSession.objects.get(user_id=request.user)
    # if ShoppingSession.objects.filter(user_id=request.user).exists():
    #     session = ShoppingSession.objects.filter(user_id=request.user)
    # else:
    #     ShoppingSession.objects.create
    print("oldu ")
    if request.method == 'POST':
    
        orderQuantity= request.POST.get('quantity')
    
        if Cart.objects.filter(product_id=product, user_id=request.user, ).exists():
            cartObj = Cart.objects.get(product_id=product, user_id=request.user)
            qty = cartObj.quantity
            cartObj.quantity = qty+int(orderQuantity)
            cartObj.save()
            
        else:
            Cart.objects.create(product_id=product,quantity=orderQuantity,user_id=request.user,session_id = session)
    
    else : 
        orderQuantity = 1
        if Cart.objects.filter(product_id=product, user_id=request.user, ).exists():
            cartObj = Cart.objects.get(product_id=product, user_id=request.user)
            qty = cartObj.quantity
            cartObj.quantity = qty+int(orderQuantity)
            cartObj.save()
            
        else:
            Cart.objects.create(product_id=product,quantity=orderQuantity,user_id=request.user,session_id = session)
        
       
    

    priceTotal.total += price*int(orderQuantity)
    priceTotal.save()
    return HttpResponseRedirect(url)

@login_required
def removeCart(request,slug):
    item = Product.objects.get(slug = slug)
    product = Cart.objects.get(user_id = request.user, product_id = item)
    price = item.price*int(product.quantity)
    session = ShoppingSession.objects.get(user_id=request.user)
    session.total -= price
    session.save()
    
    product.delete()
    url = request.META.get('HTTP_REFERER')
    return HttpResponseRedirect(url)

@login_required
def placeOrder(request,id):
    # session = ShoppingSession.objects.get(user_id=request.user)
    # priceTotal = ShoppingSession.objects.get(user_id=request.user)
    # # if ShoppingSession.objects.filter(user_id=request.user).exists():
    # #     session = ShoppingSession.objects.filter(user_id=request.user)
    # # else:
    # #     ShoppingSession.objects.create
    # if request.method == 'POST':
    #     orderQuantity= request.POST.get('quantity')
    
    #     if Cart.objects.filter(product_id=product, user_id=request.user, ).exists():
    #         cartObj = Cart.objects.get(product_id=product, user_id=request.user)
    #         qty = cartObj.quantity
    #         cartObj.quantity = qty+int(orderQuantity)
    #         cartObj.save()
            
    #     else:
    #         Cart.objects.create(product_id=product,quantity=orderQuantity,user_id=request.user,session_id = session)

    # priceTotal.total += price*int(orderQuantity)
    # priceTotal.save()

        
    
    # return JsonResponse({'status':'done'})
    pass
   

def change_password(request):
     if request.method == 'POST':
         form = PasswordChangeForm(request.user, request.POST)
         if form.is_valid():
             user = form.save()
             update_session_auth_hash(request, user)  # Important!
             messages.success(request, 'Your password was successfully updated!')
             return redirect('profile')
         else:
             messages.error(request, 'Please correct the error below.')
     else:
         form = PasswordChangeForm(request.user)
     return render(request, 'profile.html', {
         'changePasswordForm': form
     })
    
def orderPage(request):
    session = ShoppingSession.objects.get(user_id = request.user)
    products = Cart.objects.filter(user_id=request.user,ordered=False)
    order =  Orders.objects.get_or_create(user_id = request.user)
    
    for item in products :
        OrderItems.objects.create(product_id=item.product_id,quantity = item.quantity)
        item.delete()
    session.total = 0
    return render(request, 'order-page.html')

