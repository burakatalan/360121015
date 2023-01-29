from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm
from .models import UserAdress,UserInf,ContactForm,Cart
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm


class ContactForm(ModelForm):
    class Meta:
        model = ContactForm
        fields = ('name', 'email','subject','message')
        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'email': forms.TextInput(attrs={'class': 'form-control'}),
                'subject': forms.TextInput(attrs={'class': 'form-control'}),
                'message':forms.TextInput(attrs={'class': 'form-control'}),
        }




class PersonForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', )

        widget = {
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'surname': forms.TextInput(attrs={'class': 'form-control'}),
                
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))


class QtyForm(forms.Form):
    qty = forms.IntegerField(label='qty', widget=forms.TextInput(attrs={'id':'quantity','class': 'form-control'}))
    
