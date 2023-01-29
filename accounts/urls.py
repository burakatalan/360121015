from django.urls import path
from . import views
from .views import PasswordsChangeView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register,
         name='register'),

    path('logout/', views.logoutaccount,
         name='logoutaccount'),

    path('login/', views.loginaccount,
         name='login'),

    path('change-password/', PasswordsChangeView.as_view(template_name='change-password.html'),name='change_password'),

    path('profile/', views.profile,name='profile'),

    path('payment/',views.payment,name='payment'),

    path('address/',views.address,name='address'),

    path('orders/',views.orders, name ='orders')
]
