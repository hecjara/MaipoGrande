from django.shortcuts import render, redirect
from django.db import connection
from .forms import CustomUserForm, CustomUserForm2
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate
from .models import PERSONA, PAIS, PRODUCTO, SOLICITUD_COMPRA, ESTADO_SOLICITUD, DETALLE_SOLICITUD
import cx_Oracle
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import date
from datetime import datetime

# Create your views here.


def home(request):

    return render(request, "core/home.html")



def links(request):
    return render(request, "core/links.html")

@login_required
def solicitud_compra(request):

    soli = SOLICITUD_COMPRA.objects.filter(id_usuario=request.user)

    return render(request, 'core/solicitud_compra.html', {
        'soli':soli
    })

@login_required
def listar_productos(request, id): #id de la solicitud

    det = DETALLE_SOLICITUD.objects.filter(id_solicitud=id)


    return render(request, 'core/listar_productos.html', {
        'det':det
    })


@login_required
def agregar_producto(request, id):
    
    solicitud = SOLICITUD_COMPRA.objects.get(id_solicitud=id)
    prod = PRODUCTO.objects.all()
    


    variables = {
        'prod':prod,
        'solicitud':solicitud
    }

    if request.POST:

        detalle = DETALLE_SOLICITUD()
        producto = PRODUCTO()
        soli = SOLICITUD_COMPRA()
        detalle.cantidad = request.POST.get('cant')
        
        soli.id_solicitud = request.POST.get('idsoli')
        detalle.id_solicitud = soli

        producto.id_producto = request.POST.get('cboproducto')
        detalle.id_producto = producto

        try:
            detalle.save()
            variables['mensaje'] = 'El producto ha sido agregado a la solicitud'
        except:
            variables['mensaje'] = 'Error al intentar agregar el producto a la solicitud'

    return render(request, 'core/agregar_producto.html', variables)


@login_required
def formulario_solicitud(request):

    est = 1

    soli = SOLICITUD_COMPRA()
    soli.fecha_pedido = datetime.now()
    soli.direccion_destino = request.POST.get('direccion')
    soli.fecha_min = request.POST.get('min')
    soli.fecha_max = request.POST.get('max')   
    soli.id_usuario = request.user

    estado = ESTADO_SOLICITUD()
    estado.id_estado = est
    soli.id_estado = estado

    try:
        soli.save()
        messages.success(request, 'Lista agregada correctamente')
    except:
        messages.error(request, 'No se ha podido agregar la lista')

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



