from django.contrib import admin
from .models import Category
from .models import ContactForm
# Register your models here.

from .models import Cart
from .models import Product
from .models import Media
from .models import Category
from .models import UserInf
from .models import UserAdress
from .models import Orders
from .models import subCategory
from .models import Newsteller
from .models import UserPayment
from .models import ShoppingSession
from .models import OrderItems


admin.site.register(UserInf)
admin.site.register(UserAdress)
admin.site.register(UserPayment)
admin.site.register(ShoppingSession)
admin.site.register(Cart)
admin.site.register(Orders)
admin.site.register(OrderItems)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(subCategory)
admin.site.register(Media)
admin.site.register(Newsteller)
admin.site.register(ContactForm)

class Shop(admin.ModelAdmin):
    list_filter = ("category",)

class ContactForm(admin.ModelAdmin):
    list_filter = ('name', 'email','subject','message')

class AddressFrom(admin.ModelAdmin):
    list_display=('name', 'address1', 'address2','city','country','zip_code','title',)

class PaymentForm(admin.ModelAdmin):
    list_display= ('name','card_no', 'cvv', 'expiration','title')

class UserInfForm(admin.ModelAdmin):
    list_display = ('phone')







