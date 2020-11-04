from django import forms
from django.forms import ModelForm, ModelChoiceField, inlineformset_factory
from .models import *
import datetime
from django.contrib.auth.forms import UserCreationForm


class CustomUserForm(UserCreationForm):
    rut = forms.CharField(required=False, label='RUT', min_length=9, max_length=10, widget=forms.TextInput(attrs={"class":"form-control"}))
    dni = forms.CharField(required=False, label='DNI', min_length=10, max_length=20, widget=forms.TextInput(attrs={'placeholder':'Ingrese solo en caso de ser extranjero', "class":"form-control"}))
    fecha_nacimiento = forms.DateField(widget=forms.SelectDateWidget(years=range(1920,2021), attrs=({'style': 'width: 20%; display: inline-block;', "class":"mr-2 form-control"})), required=True, label='Fecha de nacimiento')
    telefono = forms.IntegerField(required=True, label='Teléfono', widget=forms.NumberInput(attrs={"class":"form-control"}))
    pais = forms.ModelChoiceField(PAIS.objects.all(), initial=42, required=True, widget=forms.Select(attrs={"class":"form-control"}))
    first_name = forms.CharField(required=True, label='Nombres', min_length=2, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(required=True, label='Apellidos', min_length=2, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(required=True, label='Email', min_length=5, max_length=100, widget=forms.EmailInput(attrs={"class":"form-control"}))
    direccion = forms.CharField(required=False, label='Dirección', min_length=5, max_length=100, widget=forms.TextInput(attrs={"class":"form-control"}))
    

    class Meta:
        model = User
        fields = ['rut', 'dni','first_name', 'last_name', 'email', 'telefono', 'fecha_nacimiento', 'direccion','pais', 'username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'autofocus': False, 'class':'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})



class CustomUserForm2(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

        


