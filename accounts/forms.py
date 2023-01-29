from django import forms
from django.forms import ModelForm, TextInput
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from shop.models import UserPayment,UserAdress,UserInf


class UserCreateForm(UserCreationForm):
        first_name = forms.CharField(max_length=101)
        last_name = forms.CharField(max_length=101)
        email = forms.EmailField()

        def __init__(self, *args, **kwargs):
            super(UserCreateForm, self).__init__(*args,
                                                        **kwargs)
            phone_number = forms.CharField(max_length=101)
            for fieldname in ['username', 'first_name', 'last_name', 'email','password1', 'password2']:
                    self.fields[fieldname].help_text = None
                    self.fields[fieldname].widget.attrs.update(
                    {'class': 'form-control'}) 

class PasswordChangingForm(PasswordChangeForm):
        old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
        new_password1 = forms.CharField(max_length=101, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
        new_password2 = forms.CharField(max_length=101, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))

        class Meta:
               Model = User
               fields = ['old_password', 'new_password1', 'new_password2']

class PaymentForm(forms.ModelForm):
        class Meta:
                model = UserPayment
                fields = ['name','card_no', 'cvv', 'expiration','title']
                widgets = { 'name' : TextInput(attrs={'class':'form-control'}),
                            'card_no' : TextInput(attrs={'class':'form-control'}),
                            'cvv' : TextInput(attrs={'class':'form-control'}),
                            'expiration' : TextInput(attrs={'class':'form-control'}),
                            'title' : TextInput(attrs={'class':'form-control'}),
                           
                }

class AddressForm(forms.ModelForm):
        class Meta:
                model = UserAdress
                fields = ['title', 'name', 'address1', 'address2','city','country','zip_code']
                widgets = { 'name' : TextInput(attrs={'class':'form-control'}),
                            'address1' : TextInput(attrs={'class':'form-control'}),
                            'address2' : TextInput(attrs={'class':'form-control'}),
                            'city' : TextInput(attrs={'class':'form-control'}),
                            'country' : TextInput(attrs={'class':'form-control'}),
                            'zip_code' : TextInput(attrs={'class':'form-control'}),
                            'title' : TextInput(attrs={'class':'form-control'}),

                }
class UserInfForm(forms.ModelForm):
        class Meta:
                model = UserInf
                fields = ['phone']
                widgets = { 'phone' : TextInput(attrs={'class':'form-control'}),
                            
                }
                 