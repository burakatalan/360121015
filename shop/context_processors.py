from .models import Cart,ShoppingSession
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User






def cartObjects(request):
  if (User=="AnonymousUser"):
     Console.log(User)
  else:  
     objects = Cart.objects.filter(user_id=request.user,ordered=False)
     total = ShoppingSession.objects.get(user_id=request.user)
   
     context = {
         'cartObjects': objects,
         'total': total.total
        
     }
     return context
