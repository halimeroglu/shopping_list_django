from django import forms
from .models import Product

class ListForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name","category") 
        widget = {
            'name' : forms.TextInput(attrs={'class':"form-control"}),
            'category' : forms.TextInput(attrs={'class':"form-control"}),
        }