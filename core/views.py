from django.shortcuts import render, redirect
from django.db import connection
from .forms import CustomUserForm, CustomUserForm2
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate
from .models import PERSONA, PAIS
import cx_Oracle
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.


def home(request):

    return render(request, "core/home.html")



def links(request):
    return render(request, "core/links.html")


def solicitud_compra(request):
    return render(request, "core/solicitud_compra.html")

def formulario_solicitud(request):
    return render(request, "core/formulario_solicitud.html")

def registro_minorista(request):

    data = {"form": CustomUserForm()}

    if request.method == "POST":
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()

            per = PERSONA()

            usu = User.objects.last()


            per.id_usuario = usu
            per.rut = formulario.cleaned_data["rut"]
            per.dni = formulario.cleaned_data["dni"]
            per.nombres = formulario.cleaned_data["first_name"]
            per.apellidos = formulario.cleaned_data["last_name"]
            per.email = formulario.cleaned_data["email"]
            per.fecha_nacimiento = formulario.cleaned_data["fecha_nacimiento"]
            per.telefono = formulario.cleaned_data["telefono"]
            per.direccion = formulario.cleaned_data["direccion"]
            pa = PAIS()
            pa.id_pais = formulario["pais"].value()
            per.id_pais = pa

            per.save()

            # autenticar al usuario y redirigirlo al inicio
            username = formulario.cleaned_data["username"]
            password = formulario.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect(to="home")
    return render(request, "registration/registro_minorista.html", data)


def registro_usuario(request, cod):

    data = {"form2": CustomUserForm2()}

    if request.method == 'POST':
        formulario = CustomUserForm2(request.POST)
        if formulario.is_valid():
            formulario.save()
            usu = User.objects.last()

            persona = PERSONA()

            per = PERSONA.objects.get(codigo_activacion=cod)
        
            per.id_usuario = usu

            per.save()
            
            #autenticar al usuario y redirigirlo al inicio
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='home')

    return render(request, "registration/registro_usuario.html", data)



def buscar_persona(cod, rut, dni):

    persona = PERSONA()
    persona = PERSONA.objects.filter(codigo_activacion=cod).filter(rut=rut).filter(dni=dni)
    return persona




def codigo_activacion(request):
    if request.POST:
        cod = request.POST.get("codigo")
        rut = request.POST.get("rut")
        dni = request.POST.get("dni")
    
        perso = buscar_persona(cod, rut, dni)

        if perso:
            messages.success(request, 'Usuario encontrado!')
            return render(request, "registration/codigo_activacion.html", {
                "perso": perso
                })
        else:
            messages.error(request, 'Usuario no existente o código de activación no valido')
            return render(request,"registration/codigo_activacion.html")
    return render(request, "registration/codigo_activacion.html")







