from django import forms
from django.forms import ModelForm
from myapp.models import *

class ItensProduct(forms.ModelForm):
    class Meta:

        model = Product
        fields = "__all__"
        labels = {
            "name": "Nome",
            "descript": "Descrição",
            "price":"Preço",
            "path": "Imagem",
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Nome do item",
                }
            ),
            'descript': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Escreva uma breve descrição",
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Escreva o preço do item",
                }
            ),
            'path': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Imagem",
                }
            ),
        }
    

class ItensCart(forms.ModelForm):
    class Meta:

        model = Cart
        fields = "__all__"
        labels = {
            "name": "Nome",
            "descript": "Descrição",
            "price":"Preço",
            "path": "Imagem",
        },
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Nome do item",
                }
            ),
        
        }
