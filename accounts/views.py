from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate , logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from .forms import UserCreateForm,PasswordChangingForm,PaymentForm,AddressForm,UserInfForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from shop.models import Cart, Category, Newsteller,Product, ShoppingSession,UserInf,UserPayment,OrderItems,Orders
from django.http import HttpResponseRedirect



def register(request):
   
    if request.method == 'GET':
        return render(request, 'register.html',
                      {'form': UserCreateForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                    user = User.objects.create_user(
                    request.POST['username'],
                    password=request.POST['password1'])
                    user.first_name = request.POST['first_name']
                    user.last_name = request.POST['last_name']
                    user.email = request.POST['email']
                    
                  
                    user.save()
                    login(request, user)
                    ShoppingSession.objects.create(user_id=request.user)
                    return redirect('home')
            except IntegrityError:
             return render(request,
             'register.html', 
              {'form':UserCreateForm,
            'error':'Username already taken. Choose new username.'})
        else:
            return render(request, 'register.html',{'form': UserCreateForm, 'error': 'Passwords do not match'})

def logoutaccount(request): 
 logout(request)
 return redirect('home')

def loginaccount(request): 
        if request.method == 'GET':
            return render(request, 'login.html', 
                            {'form':AuthenticationForm})
        else:
            user = authenticate(request,
             username=request.POST['username'],
             password=request.POST['password']) 
            if user is None:
                return render(request,'login.html',{'form': AuthenticationForm(),'error': 'username and password do not match'})
            else: 
                login(request,user)
                return redirect('home')


class PasswordsChangeView(PasswordChangeView):

    form_class = PasswordChangingForm
    success_url = reverse_lazy('accounts/profile')
    

@login_required
def profile(request):
    context=dict()
    user= request.user
    username= request.user.username
    email= request.user.email
    name= request.user.first_name
    surname= request.user.last_name
    phone = UserInf.objects.filter(user_id=request.user)
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        form = UserInfForm(request.POST)
        if form.is_valid():
            userpn = form.save(commit=False)
            userpn.user_id = user
            userpn.save()
            return HttpResponseRedirect(url)
    else:
        context['form'] = UserInfForm()
   
    context ={
      
        'username': username,
        'email': email,
        'name': name,
        'surname': surname,
        'phone':phone,
       

    }
    
    return render(request, 'profile.html',context) 

@login_required
def payment(request):
    context=dict()
    url = request.META.get('HTTP_REFERER')
    user = request.user
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user_id = user
            payment.save()
            return HttpResponseRedirect(url)
    else:
        context['form'] = PaymentForm()
    

    return render(request, 'payment.html',context) 

@login_required
def address(request):
    context=dict()
    url = request.META.get('HTTP_REFERER')
    user = request.user
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user_id = user
            address.save()
            return HttpResponseRedirect(url)
    else:
        context['form'] = AddressForm()
    
    return render(request, 'address.html',context,) 

@login_required
def orders(request):
    order = Orders.objects.get(user_id = request.user)
    items = OrderItems.objects.filter(order_id = order)
    context = {
        'items' : items
    }
    return render(request,'orders.html', context )