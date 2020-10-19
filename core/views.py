from django.shortcuts import render, redirect
from django.db import connection
from .forms import CustomUserForm, CustomUserForm2
from django.contrib.auth.decorators import (
    login_required,
    permission_required,
    user_passes_test,
)
from django.contrib.auth import login, authenticate
from .models import (
    PERSONA,
    PAIS,
    PRODUCTO,
    SOLICITUD_COMPRA,
    ESTADO_SOLICITUD,
    DETALLE_SOLICITUD,
    TIPO_PERSONA,
    PROCESO_VENTA,
    HISTORIAL_POSTULACION,
    PRODUCTO_BODEGA,
    CONCLUSION,
)
import cx_Oracle
from django.contrib.auth.models import User, Group
from django.contrib import messages
from datetime import date
from datetime import datetime
from django.db import connection
from django.core.files.base import ContentFile
import base64
from django.utils import timezone

# Create your views here.


def home(request):
    return render(request, "core/home.html")


def rechazar_oferta(request, id_solicitud):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_RECHAZAR_OFERTA", [id_solicitud, salida])
    res = salida.getvalue()

    if res == 1:
        messages.success(
            request,
            "La oferta ha sido rechazada.",
            extra_tags="alert alert-success",
        )
    else:
        messages.error(
            request,
            "Error al intentar rechazar la oferta.",
            extra_tags="alert alert-danger",
        )
    return redirect("solicitud_compra")

def aceptar_oferta(request, id_solicitud):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_ACEPTAR_OFERTA", [id_solicitud, salida])
    res = salida.getvalue()

    if res == 1:
        messages.success(
            request,
            "La oferta ha sido aceptada, ahora pasara a la fase de subasta de transporte.",
            extra_tags="alert alert-success",
        )
    else:
        messages.error(
            request,
            "Error al intentar aceptar la oferta.",
            extra_tags="alert alert-danger",
        )
    return redirect("solicitud_compra")


def resultado_solicitud(request, id_solicitud):

    data = {
        'ganadores': listar_ganadores(id_solicitud),
        'total': obtener_valor_total(id_solicitud),
    }

    return render(request, "core/resultado_solicitud.html", data)


def obtener_valor_total(id_solicitud):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_VALOR_TOTAL", [id_solicitud, out_cur])

    lista = []

    for fila in out_cur:
        lista.append(fila)
    return lista

def listar_ganadores(id_solicitud):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_GANADORES", [id_solicitud, out_cur])

    lista = []

    for fila in out_cur:
        lista.append(fila)
    return lista

@login_required
def procesos_venta(request):  # listar procesos de ventas activos
    id_usuario = request.user.id

    data = {
        "procesos": listar_procesoventaconproductoscoincidentes(id_usuario),
    }

    return render(request, "core/procesos_venta.html", data)

def listar_procesoventaconproductoscoincidentes(id_usuario):  # listar procesos de venta que tengan un producto que el proveedor tenga en bodega
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTARPROCESOSXPRODUCTOSQUETENGO", [id_usuario, out_cur])

    lista = []

    for fila in out_cur:
        lista.append(fila)
    return lista

@login_required
def producto_procesoventa(request, id_detalle, id_proceso, id_producto):

    id_usuario = request.user.id

    data = {
        "producto": ver_productoProceso(id_detalle),
        "prod_bod": listar_prod_bod(id_producto, id_usuario),
        "historial": listar_historial_ofertas(id_proceso, id_producto),
        "mejoroferta": listar_mejor_oferta(id_proceso, id_producto),
    }

    if request.POST:

        historial = HISTORIAL_POSTULACION()
        historial.oferta = request.POST.get("ofertatxt")
        historial.cantidad = request.POST.get("cantidadtxt")

        now = timezone.now()
        # now = datetime.now()
        historial.fecha_oferta = now

        pv = PROCESO_VENTA()
        pv.id_proceso = request.POST.get("id_proceso")
        historial.id_proceso = pv

        pb = PRODUCTO_BODEGA()
        pb.id_prod_bod = request.POST.get("cboprodbod")
        historial.id_prod_bod = pb

        user = User()
        user.id = request.user.id
        historial.id_usuario = user

        conclusion = CONCLUSION()
        conclusion.id_conclusion = 0
        historial.id_conclusion  = conclusion

        try:
            historial.save()
            messages.success(
                request,
                "Oferta realizada correctamente.",
                extra_tags="alert alert-success",
            )
        except Exception as e:
            messages.error(
                request,
                "Error al realizar la oferta " + str(e),
                extra_tags="alert alert-danger",
            )
        return redirect(
            "producto_procesoventa", id_detalle, id_proceso, id_producto
        )

    return render(request, "core/producto_procesoventa.html", data)


def listar_prod_bod(id_producto, id_usuario):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_PROD_BOD", [id_producto, id_usuario, out_cur])

    lista = []

    for fila in out_cur:
        lista.append(fila)
    return lista

def ver_productoProceso(id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_PRODUCTOPROCESO", [id, out_cur])

    lista = []

    for fila in out_cur:
        lista.append(fila)
    return lista

def listar_historial_ofertas(id_proceso, id_producto):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_HISTORIAL", [id_proceso, id_producto, out_cur])

    lista = []

    for fila in out_cur:
        lista.append(fila)
    return lista

def actualizar_pedidorecibido(request, id_solicitud):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_PEDIDO_RECIBIDO", [id_solicitud, salida])
    res = salida.getvalue()

    if res == 1:
        messages.success(
            request,
            "Estado actualizado correctamente.",
            extra_tags="alert alert-success",
        )
    else:
        messages.error(
            request,
            "Error al intentar actualizar el estado.",
            extra_tags="alert alert-danger",
        )
    return redirect("solicitud_compra")


def actualizar_pedidoanulado(request, id_solicitud):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_PEDIDO_ANULADO", [id_solicitud, salida])
    res = salida.getvalue()

    if res == 1:
        messages.success(
            request,
            "La solicitud ha sido anulada correctamente.",
            extra_tags="alert alert-success",
        )
    else:
        messages.error(
            request,
            "Error al intentar anular la solicitud.",
            extra_tags="alert alert-danger",
        )
    return redirect("solicitud_compra")


# @login_required
# def mis_productos(request):

#     id_usuario = request.user.id

#     data = {"procesos": listar_misproductos(id_usuario)}

#     return render(request, "core/mis_productos.html", data)


# def listar_misproductos(id_usuario):
#     django_cursor = connection.cursor()
#     cursor = django_cursor.connection.cursor()
#     out_cur = django_cursor.connection.cursor()

#     cursor.callproc("SP_LISTAR_MISPRODUCTOS", [id_usuario, out_cur])

#     lista = []

#     for fila in out_cur:
#         lista.append(fila)
#     return lista

@login_required
def modificar_datos_personales(request, id):

    persona = PERSONA.objects.get(id_usuario=id)
    pais = PAIS.objects.all()

    variables = {"pais": pais, "persona": persona}

    if request.POST:
        persona = PERSONA()
        tp = 3
        usu = User()
        usu.id = request.POST.get("txtid_usuario")

        persona.id_usuario_id = usu
        persona.rut = request.POST.get("txtrut")
        persona.dni = request.POST.get("txtdni")
        persona.id_persona = request.POST.get("txtpersona")
        persona.nombres = request.POST.get("txtnombres")
        persona.apellidos = request.POST.get("txtapellidos")
        persona.fecha_nacimiento = request.POST.get("txtfecha")
        persona.telefono = request.POST.get("txttelefono")
        persona.email = request.POST.get("txtemail")
        persona.direccion = request.POST.get("txtdireccion")

        pais = PAIS()
        pais.id_pais = request.POST.get("cbopais")
        persona.id_pais = pais

        tipo = TIPO_PERSONA()
        tipo.id_tipo = tp
        persona.id_tipo = tipo

        try:
            persona.save()
            messages.success(
                request,
                "Sus datos personales han sido modificados correctamente.",
                extra_tags="alert alert-success",
            )
        except Exception as e:
            messages.error(
                request,
                "Error al intentar modificar sus datos personales" + str(e),
                extra_tags="alert alert-danger",
            )
        return redirect("perfil_usuario", request.user.id)

    return render(request, "core/modificar_datos_personales.html", variables)


@login_required
def perfil_usuario(request, id):
    persona = PERSONA.objects.get(id_usuario=id)
    pais = PAIS.objects.all()

    return render(
        request, "core/perfil_usuario.html", {"persona": persona, "pais": pais}
    )


@login_required
def solicitud_compra(request):

    id_usuario = request.user.id

    data = {
        'soli': listar_solicitudes(id_usuario)
    }

    return render(request, "core/solicitud_compra.html", data)


def listar_solicitudes(id_usuario):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_SOLICITUDES", [id_usuario, out_cur])

    lista = []

    for fila in out_cur:
        lista.append(fila)
    return lista


@login_required
def anular_solicitud(request, id):
    solicitud = SOLICITUD_COMPRA.objects.get(pk=id)

    estado = ESTADO_SOLICITUD()
    estado.id_estado = 9  # 9: anulado
    solicitud.id_estado = estado

    try:
        solicitud.save()
        messages.success(
            request,
            "La solicitud ha sido anulada correctamente.",
            extra_tags="alert alert-success",
        )
    except Exception as e:
        messages.error(
            request,
            "Error al intentar agregar el producto a la solicitud" + str(e),
            extra_tags="alert alert-danger",
        )
    return redirect("solicitud_compra")


@login_required
def eliminar_detalleproducto(request, id):
    detalle = DETALLE_SOLICITUD.objects.get(pk=id)

    try:
        detalle.delete()
        messages.success(
            request,
            "Producto eliminado correctamente.",
            extra_tags="alert alert-success",
        )
    except Exception as e:
        messages.error(
            request,
            "Error al intentar eliminar el producto" + str(e),
            extra_tags="alert alert-danger",
        )
    return redirect("listar_productos", detalle.id_solicitud.id_solicitud)


@login_required
def modificar_detalleproducto(request, id):
    detalle = DETALLE_SOLICITUD.objects.get(pk=id)
    productos = PRODUCTO.objects.all()

    variables = {"detalle": detalle, "productos": productos}

    if request.POST:
        detalle = DETALLE_SOLICITUD()

        detalle.id_detalle = request.POST.get("iddetalle")
        detalle.cantidad = request.POST.get("cant")

        solicitud = SOLICITUD_COMPRA()
        solicitud.id_solicitud = request.POST.get("idsolicitud")
        detalle.id_solicitud = solicitud

        producto = PRODUCTO()
        producto.id_producto = request.POST.get("cboproducto")
        detalle.id_producto = producto

        try:
            detalle.save()
            messages.success(
                request,
                "Producto modificado correctamente.",
                extra_tags="alert alert-success",
            )

        except Exception as e:
            messages.error(
                request,
                "Error al intentar modificar el producto" + str(e),
                extra_tags="alert alert-danger",
            )
        return redirect("listar_productos", detalle.id_solicitud.id_solicitud)

    return render(request, "core/modificar_detalleproducto.html", variables)


@login_required
def listar_productos(request, id):  # id de la solicitud

    det = DETALLE_SOLICITUD.objects.filter(id_solicitud=id)
    variables = {"det": det}

    return render(request, "core/listar_productos.html", variables)


@login_required
def agregar_producto(request, id):

    solicitud = SOLICITUD_COMPRA.objects.get(id_solicitud=id)
    prod = PRODUCTO.objects.all()

    variables = {"prod": prod, "solicitud": solicitud}

    if request.POST:

        detalle = DETALLE_SOLICITUD()
        producto = PRODUCTO()
        soli = SOLICITUD_COMPRA()
        detalle.cantidad = request.POST.get("cant")

        soli.id_solicitud = request.POST.get("idsoli")
        detalle.id_solicitud = soli

        producto.id_producto = request.POST.get("cboproducto")
        detalle.id_producto = producto

        try:
            detalle.save()
            messages.success(
                request,
                "Producto agregado a la solicitud correctamente",
                extra_tags="alert alert-success",
            )

        except Exception as e:
            messages.error(
                request,
                "Error al intentar agregar el producto a la solicitud" + str(e),
                extra_tags="alert alert-danger",
            )
        return redirect("listar_productos", solicitud.id_solicitud)

    return render(request, "core/agregar_producto.html", variables)


@login_required
def formulario_solicitud(request):

    if request.POST:
        est = 1

        soli = SOLICITUD_COMPRA()
        soli.fecha_pedido = datetime.now()
        soli.direccion_destino = request.POST.get("direccion")
        soli.fecha_min = request.POST.get("min")
        soli.fecha_max = request.POST.get("max")
        soli.id_usuario = request.user

        estado = ESTADO_SOLICITUD()
        estado.id_estado = est
        soli.id_estado = estado

        try:
            soli.save()
            messages.success(
                request,
                "Lista agregada correctamente",
                extra_tags="alert alert-success",
            )

        except Exception as e:
            messages.error(
                request,
                "No se ha podido agregar la lista" + str(e),
                extra_tags="alert alert-danger",
            )
        return redirect("solicitud_compra")

    return render(request, "core/formulario_solicitud.html")


def registro_minorista(request):

    data = {"form": CustomUserForm()}
    tp = 3
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

            tipo = TIPO_PERSONA()
            tipo.id_tipo = tp
            per.id_tipo = tipo

            per.save()

            grupo = Group.objects.get(name="CompradorMinorista")
            grupo.user_set.add(usu)

            # autenticar al usuario y redirigirlo al inicio
            username = formulario.cleaned_data["username"]
            password = formulario.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect(to="home")
    return render(request, "registration/registro_minorista.html", data)


def registro_usuario(request, cod):

    data = {"form2": CustomUserForm2()}

    if request.method == "POST":
        formulario = CustomUserForm2(request.POST)
        if formulario.is_valid():
            formulario.save()
            usu = User.objects.last()

            per = PERSONA.objects.get(codigo_activacion=cod)

            per.id_usuario = usu

            per.save()

            if per.id_tipo.nombre_tipo == "CompradorMayorista":
                grupo = Group.objects.get(name="CompradorMayorista")
                grupo.user_set.add(usu)
            elif per.id_tipo.nombre_tipo == "Proveedor":
                grupo = Group.objects.get(name="Proveedor")
                grupo.user_set.add(usu)
            elif per.id_tipo.nombre_tipo == "Transportista":
                grupo = Group.objects.get(name="Transportista")
                grupo.user_set.add(usu)

            # autenticar al usuario y redirigirlo al inicio
            username = formulario.cleaned_data["username"]
            password = formulario.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to="home")

    return render(request, "registration/registro_usuario.html", data)


def buscar_persona(cod, rut, dni):

    persona = PERSONA()
    persona = (
        PERSONA.objects.filter(codigo_activacion=cod).filter(rut=rut).filter(dni=dni)
    )
    return persona


def codigo_activacion(request):
    if request.POST:
        cod = request.POST.get("codigo")
        rut = request.POST.get("rut")
        dni = request.POST.get("dni")

        perso = buscar_persona(cod, rut, dni)

        if perso:
            messages.success(
                request, "Usuario encontrado!", extra_tags="alert alert-success"
            )
            return render(
                request, "registration/codigo_activacion.html", {"perso": perso}
            )
        else:
            messages.error(
                request,
                "Usuario no existente o código de activación no valido",
                extra_tags="alert alert-danger",
            )
            return render(request, "registration/codigo_activacion.html")
    return render(request, "registration/codigo_activacion.html")

