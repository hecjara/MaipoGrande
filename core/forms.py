from django import forms
from django.forms import ModelForm, ModelChoiceField
from .models import *
import datetime
from django.contrib.auth.forms import UserCreationForm



class CustomUserForm(UserCreationForm):
    rut = forms.CharField(required=False, label='RUT', min_length=9, max_length=10)
    dni = forms.CharField(required=False, label='DNI', min_length=10, max_length=20, widget=forms.TextInput(attrs={'placeholder':'Ingrese solo en caso de ser extranjero'}))
    fecha_nacimiento = forms.DateField(widget=forms.SelectDateWidget(years=range(1920,2021)), required=True, label='Fecha de nacimiento')
    telefono = forms.IntegerField(required=True, label='Teléfono')
    pais = forms.ModelChoiceField(PAIS.objects.all(), initial=42, required=True)
    first_name = forms.CharField(required=True, label='Nombres', min_length=2, max_length=100)
    last_name = forms.CharField(required=True, label='Apellidos', min_length=2, max_length=100)
    email = forms.EmailField(required=True, label='Email', min_length=5, max_length=100)
    direccion = forms.CharField(required=False, label='Dirección', min_length=5, max_length=100)


    class Meta:


        model = User
        fields = ['rut', 'dni','first_name', 'last_name', 'email', 'telefono', 'fecha_nacimiento', 'direccion','pais', 'username', 'password1', 'password2']



class CustomUserForm2(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

        


