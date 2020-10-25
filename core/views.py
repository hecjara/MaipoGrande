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
    HISTORIAL_SUBASTA,
    SUBASTA_TRANSPORTE,
)
import cx_Oracle
from django.contrib.auth.models import User, Group
from django.contrib import messages
from datetime import date
from datetime import datetime
import datetime
from django.db import connection
from django.core.files.base import ContentFile
import base64
from django.utils import timezone

# Create your views here.


def home(request):
    return render(request, "core/home.html")

def contacto(request):
    return render(request, "core/contacto.html")


##################################################################################################
####                                                                                          ####
####                       MODULO DE VENTA LOCAL                                              ####
####                                                                                          ####
##################################################################################################


def venta_local(request):

    # data = {
    #     'ventalocal': listar_productos_venta_local()
    # }

    return render(request, "core/venta_local.html")


# def listar_productos_venta_local():
#     django_cursor = connection.cursor()
#     cursor = django_cursor.connection.cursor()
#     out_cur = django_cursor.connection.cursor()

#     cursor.callproc("SP_LISTAR_PRODUCTOS_VENTA_LOCAL", [out_cur])

#     lista = []

#     for fila in out_cur:
#         lista.append(fila)
#     return lista


##################################################################################################
####                                                                                          ####
####                       FIN MODULO VENTA LOCAL                                             ####
####                                                                                          ####
##################################################################################################

##################################################################################################
####                                                                                          ####
####                       MODULO DE SUBASTAS DE TRANSPORTE                                   ####
####                                                                                          ####
##################################################################################################


def subastas_transporte_activas(
    request,
):  # METODO QUE LISTA SOLO LAS SUBASTAS QUE ESTAN ACTIVAS

    data = {"subastas": listar_subastas_transporte_activas()}

    return render(request, "core/subastas_transporte_activas.html", data)


def listar_subastas_transporte_activas():  # METODO PARA LLAMAR AL PROCEDIMIENTO ALMACENADO PARA LISTAR SOLO SUBASTAS ACTIVAS
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_SUBASTAS_TRANSPORTE_ACTIVAS", [out_cur])

    lista = []

    for fila in out_cur:
        lista.append(fila)
    return lista


def subasta_transporte(
    request, id_subasta
):  # METODO PARA LISTAR LOS DATOS DE LA SUBASTA SELECCIONADA
    # Y REALIZAR OFERTAS EN DICHA SUBASTA
    data = {
        "subasta": buscar_subasta_transporte(id_subasta),
        "historial": listar_historial_ofertas_transporte(id_subasta),
    }

    if request.POST:

        oferta = request.POST.get("ofertatxt")

        now = timezone.now()
        fecha_oferta = now

        id_usuario = request.user.id

        id_subasta = request.POST.get("subasta")

        salida = agregar_oferta_transporte(oferta, fecha_oferta, id_subasta, id_usuario)

        if salida == 1:
            messages.success(
                request,
                "Oferta realizada correctamente.",
                extra_tags="alert alert-success",
            )
        else:
            messages.error(
                request,
                "Error al intentar ingresar la oferta.",
                extra_tags="alert alert-danger",
            )
        return redirect("subasta_transporte", id_subasta)

    return render(request, "core/subasta_transporte.html", data)


def listar_historial_ofertas_transporte(id_subasta):  # METODO PARA LISTAR TODAS LAS OFERTAS QUE SE HAN REALIZADO EN LA SUBASTA DE TRANSPORTE
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_HISTORIAL_SUBASTA_TRANSPORTE", [id_subasta, out_cur])

    lista = []

    for fila in out_cur:
        lista.append(fila)
    return lista


def agregar_oferta_transporte(oferta, fecha_oferta, id_sub_trans, id_usuario):  # METODO PARA LLAMAR AL PROCEDIMIENTO ALMACENADO PARA REALIZAR UNA OFERTA EN LA SUBASTA DE TRANSPORTE
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc(
        "SP_AGREGAR_OFERTA_TRANSPORTE",
        [oferta, fecha_oferta, id_sub_trans, id_usuario, salida],
    )
    return salida.getvalue()


def buscar_subasta_transporte(id_subasta):  # METODO PARA LLAMAR AL PROCEDIMIENTO ALMACENADO PARA BUSCAR UNA SUBASTA EN ESPECIFICO
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_BUSCAR_SUBASTA_TRANSPORTE", [id_subasta, out_cur])

    lista = []

    for fila in out_cur:
        lista.append(fila)
    return lista


##################################################################################################
####                                                                                          ####
####                         FIN MODULO DE SUBASTAS DE TRANSPORTE                            ####
####                                                                                          ####
##################################################################################################


##################################################################################################
####                                                                                          ####
####                       MODULO DE SUBASTAS DE PRODUCTOS                                   ####
####                                                                                          ####
##################################################################################################


def rechazar_oferta(request, id_solicitud):  # METODO PARA QUE EL CLIENTE RECHAZE LAS OFERTAS
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_RECHAZAR_OFERTA", [id_solicitud, salida])
    res = salida.getvalue()

    if res == 1:
        messages.success(
            request, "La oferta ha sido rechazada.", extra_tags="alert alert-success",
        )
    else:
        messages.error(
            request,
            "Error al intentar rechazar la oferta.",
            extra_tags="alert alert-danger",
        )
    return redirect("solicitud_compra")


def aceptar_oferta(request, id_solicitud):  # METODO PARA QUE EL CLIENTE ACEPTE LAS OFERTAS
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


def resultado_solicitud(request, id_solicitud):  # METODO PARA VER LOS PRODUCTOS GANADORES DE LA SUBASTA DE PRODUCTOS

    data = {
        "ganadores": listar_ganadores(id_solicitud),
        "total": obtener_valor_total(id_solicitud),
    }

    return render(request, "core/resultado_solicitud.html", data)


def obtener_valor_total(id_solicitud):  # METODO PARA OBTENER EL VALOR DE LA SUMA DE LOS PRODUCTOS OFRECIDOS
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_VALOR_TOTAL", [id_solicitud, out_cur])

    lista = []

    for fila in out_cur:
        lista.append(fila)
    return lista


def listar_ganadores(id_solicitud):  # METODO PARA LISTAR A LOS PRODUCTOS GANADORES DE LA OFERTA
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_GANADORES", [id_solicitud, out_cur])

    lista = []

    for fila in out_cur:
        lista.append(fila)
    return lista


@login_required
def procesos_venta(request):  # METODO QUE LISTA SOLAMENTE LOS PROCESOS DE VENTA (SUBASTAS DE PRODUCTOS) ACTIVAS
    id_usuario = request.user.id

    data = {
        "procesos": listar_procesoventaconproductoscoincidentes(id_usuario),
    }

    return render(request, "core/procesos_venta.html", data)


def listar_procesoventaconproductoscoincidentes(id_usuario):  # METODO QUE LISTA SOLO LAS SUBASTAS QUE TENGAN UN PRODUCTO QUE EL PROVEEDOR TENGA EN BODEGA
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTARPROCESOSXPRODUCTOSQUETENGO", [id_usuario, out_cur])

    lista = []

    for fila in out_cur:
        lista.append(fila)
    return lista


@login_required
def producto_procesoventa(request, id_detalle, id_proceso, id_producto):  # METODO PARA LISTAR LOS DATOS DE LA SUBASTA SELECCIONADA

    id_usuario = request.user.id

    data = {
        "producto": ver_productoProceso(id_detalle),
        "prod_bod": listar_prod_bod(id_producto, id_usuario),
        "historial": listar_historial_ofertas(id_proceso, id_producto),
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
        historial.id_conclusion = conclusion

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
        return redirect("producto_procesoventa", id_detalle, id_proceso, id_producto)

    return render(request, "core/producto_procesoventa.html", data)


def listar_prod_bod(id_producto, id_usuario):  ## METODO PARA LISTAR LOS DATOS DEL PRODUCTO SELECCIONADO
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_PROD_BOD", [id_producto, id_usuario, out_cur])

    lista = []

    for fila in out_cur:
        lista.append(fila)
    return lista


def ver_productoProceso(id):  # METODO PARA LISTAR LOS DATOS DEL PRODUCTO DEL PROCESO DE VENTA
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_PRODUCTOPROCESO", [id, out_cur])

    lista = []

    for fila in out_cur:
        lista.append(fila)
    return lista


def listar_historial_ofertas(id_proceso, id_producto):  # METODO PARA LISTAR LAS OFERTAS REALIZADAS EN EL PROCESO DE VENTA
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_HISTORIAL", [id_proceso, id_producto, out_cur])

    lista = []

    for fila in out_cur:
        lista.append(fila)
    return lista


def actualizar_pedidorecibido(request, id_solicitud):  # METODO PARA QUE EL CLIENTE CAMBIE EL ESTADO A RECIBIDO
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


def actualizar_pedidoanulado(request, id_solicitud):  # METODO PARA ANULAR UNA SOLICITUD DE PROCESO DE VENTA
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


##################################################################################################
####                                                                                          ####
####                       MODULO DE PRODUCTOS EN BODEGA                                     ####
####                                                                                          ####
##################################################################################################


@login_required
def mis_productos(request):  # METODO PARA LISTAR LOS PRODUCTOS QUE TIENE EL PROVEEDOR EN BODEGA

    data = {"misproductos": listar_misproductos(request.user.id)}

    return render(request, "core/mis_productos.html", data)


def listar_misproductos(id_usuario):  # METODO PARA LLAMAR AL PROCEDIMIENTO ALMACENADO PARA LISTAR LOS PRODUCTOS DE BODEGA
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_MIS_PRODUCTOS", [id_usuario, out_cur])

    lista = []

    for fila in out_cur:
        lista.append(fila)
    return lista


def listar_productos_select():  # METODO PARA LLENAR UN SELECT CON LOS PRODUCTOS
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_PRODUCTOS", [out_cur])

    lista = []

    for fila in out_cur:
        lista.append(fila)
    return lista


@login_required
def agregar_producto_bodega(request):  # METODO PARA INGRESAR UN PRODUCTO A BODEGA

    data = {"productos": listar_productos_select()}

    if request.POST:

        id_usuario = request.user.id
        cantidad = request.POST.get("cantidadtxt")
        fecha_elaboracion = request.POST.get("fecelab")
        fecha_vencimiento = request.POST.get("fecven")
        id_producto = request.POST.get("cboproducto")
        precio_kilo = request.POST.get("preciotxt")

        salida = ingresar_producto_bodega(
            id_usuario,
            cantidad,
            fecha_elaboracion,
            fecha_vencimiento,
            id_producto,
            precio_kilo,
        )

        if salida == 1:
            messages.success(
                request,
                "Producto ingresado correctamente.",
                extra_tags="alert alert-success",
            )
        else:
            messages.error(
                request,
                "Error al intentar ingresar el producto.",
                extra_tags="alert alert-danger",
            )
        return redirect("mis_productos")

    return render(request, "core/agregar_producto_bodega.html", data)


def ingresar_producto_bodega(id_usuario, cantidad, fecha_elaboracion, fecha_vencimiento, id_producto, precio_kilo):  # METODO PARA LLAMAR AL PROCEDIMIENTO ALMACENADO PARA INGRESAR PRODUCTOS A BODEGA
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc(
        "SP_AGREGAR_PRODUCTO_BODEGA",
        [
            id_usuario,
            cantidad,
            fecha_elaboracion,
            fecha_vencimiento,
            id_producto,
            precio_kilo,
            salida,
        ],
    )
    return salida.getvalue()


def actualizar_mi_producto(request, id_prod_bod):  # METODO PARA ACTUALIZAR LOS DATOS DEL PRODUCTO EN BODEGA
    data = {
        "miproducto": datos_producto_bodega(id_prod_bod),
        "productos": listar_productos_select(),
    }

    if request.POST:
        id_prod_bod = request.POST.get("id_prod_bodtxt")
        cantidad = request.POST.get("cantidadtxt")
        precio = request.POST.get("preciotxt")

        salida = update_producto(id_prod_bod, cantidad, precio)

        if salida == 1:
            messages.success(
                request,
                "Producto actualizado correctamente.",
                extra_tags="alert alert-success",
            )
        else:
            messages.error(
                request,
                "Error al intentar actualizar el producto.",
                extra_tags="alert alert-danger",
            )
        return redirect("mis_productos")

    return render(request, "core/actualizar_mi_producto.html", data)


def update_producto(id_prod_bod, cantidad, precio):  # METODO PARA LLAMAR AL PROCEDIMIENTO ALMACENADO PARA ACTUALIZAR LOS DATOS EN BODEGA
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_ACTUALIZAR_PRODUCTO", [id_prod_bod, cantidad, precio, salida])
    return salida.getvalue()


def revisar_producto_subasta(id_prod_bod): # REVISAR PREVIAMENTE SI EL PRODUCTO ESTA EN UNA SUBASTA
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_REVISAR_PRODUCTO_EN_SUBASTA", [id_prod_bod, salida])
    return salida.getvalue()

def eliminar_producto_bodega(request, id_prod_bod):  # METODO PARA ELIMINAR UN PRODUCTO DE BODEGA
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_ELIMINAR_PRODUCTO", [id_prod_bod, salida])
    res = salida.getvalue()

    if res == 1:
        messages.success(
            request,
            "La producto ha sido eliminado correctamente.",
            extra_tags="alert alert-success",
        )
    else:
        messages.error(
            request,
            "Error al intentar eliminar el producto.",
            extra_tags="alert alert-danger",
        )
    return redirect("mis_productos")


######################################## PENDIENTE PENDIENTE PENDIENTE PENDIENTE PENDIENTE PENDIENTE PENDIENTE
def datos_producto_bodega(id_prod_bod):  # METODO PARA LISTAR LOS DATOS DEL PRODUCTO SELECCIONADO PARA MODIFICAR
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_DATOS_PRODUCTO_BODEGA", [id_prod_bod, out_cur])

    lista = []

    for fila in out_cur:
        lista.append(fila)
    return lista


######################################## PENDIENTE PENDIENTE PENDIENTE PENDIENTE PENDIENTE PENDIENTE PENDIENTE

##################################################################################################
####                                                                                          ####
####                   FIN MODULO DE SUBASTAS DE PRODUCTOS                                    ####
####                                                                                          ####
##################################################################################################

##################################################################################################
####                                                                                          ####
####                       MODULO DE SOLICITUDES DE PROCESOS DE VENTA                         ####
####                                                                                          ####
##################################################################################################


@login_required
def solicitud_compra(request):  # METODO PARA MOSTRAR MENU DE LAS SOLICITUDES

    id_usuario = request.user.id

    data = {"soli": listar_solicitudes(id_usuario)}

    return render(request, "core/solicitud_compra.html", data)


def listar_solicitudes(id_usuario):  # METODO PARA LISTAR LAS SOLICITUDES DEL USUARIO
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_SOLICITUDES", [id_usuario, out_cur])

    lista = []

    for fila in out_cur:
        lista.append(fila)
    return lista


@login_required
def anular_solicitud(request, id):  # METODO PARA ANULAR UNA SOLICITUD
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
def eliminar_detalleproducto(
    request, id_detalle
):  # METODO PARA ELIMINAR UN PRODUCTO DE LA SOLICITUD

    salida = eliminar_detalle_producto(id_detalle)

    if salida == 1:
        messages.success(
            request,
            "La producto ha sido eliminado correctamente.",
            extra_tags="alert alert-success",
        )
    else:
        messages.error(
            request,
            "Error al intentar eliminar el producto.",
            extra_tags="alert alert-danger",
        )
    return redirect("listar_productos", id_detalle)


def eliminar_detalle_producto(id_detalle):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_ELIMINAR_DETALLE_PRODUCTO", [id_detalle, salida])
    return salida.getvalue()


@login_required
def modificar_detalleproducto(
    request, id
):  # METODO PARA MODIFICAR UN PRODUCTO DE LA SOLICITUD
    detalle = DETALLE_SOLICITUD.objects.get(pk=id)
    productos = PRODUCTO.objects.all()

    variables = {"detalle": detalle, "productos": productos}

    if request.POST:

        id_detalle = request.POST.get("iddetalle")
        id_solicitud = request.POST.get("idsolicitud")
        id_producto = request.POST.get("cboproducto")
        cantidad = request.POST.get("cant")

        salida = actualizar_detalle_solicitud(
            id_detalle, id_solicitud, cantidad, id_producto
        )

        if salida == 1:
            messages.success(
                request,
                "Solicitud ingresada correctamente.",
                extra_tags="alert alert-success",
            )
        else:
            messages.error(
                request,
                "Error al intentar ingresar la solicitud.",
                extra_tags="alert alert-danger",
            )
        return redirect("listar_productos", detalle.id_solicitud.id_solicitud)

    return render(request, "core/modificar_detalleproducto.html", variables)


def actualizar_detalle_solicitud(id_detalle, id_solicitud, cantidad, id_producto):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc(
        "SP_ACTUALIZAR_DETALLE_SOLICITUD",
        [id_detalle, id_solicitud, cantidad, id_producto, salida],
    )
    return salida.getvalue()


@login_required
def listar_productos(
    request, id_solicitud
):  # METODO PARA LISTAR LOS PRODUCTOS DE LA SOLICITUD

    data = {"det": listar_productos_solicitud(id_solicitud)}

    return render(request, "core/listar_productos.html", data)


def listar_productos_solicitud(id_solicitud):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_DETALLE_SOLICITUD", [id_solicitud, out_cur])

    lista = []

    for fila in out_cur:
        lista.append(fila)
    return lista


def buscar_solicitud(id_solicitud):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_BUSCAR_SOLICITUD", [id_solicitud, out_cur])

    lista = []

    for fila in out_cur:
        lista.append(fila)
    return lista


@login_required
def agregar_producto(request, id_solicitud):  # METODO PARA AGREGAR UN PRODUCTO A LA SOLICITUD

    data = {
        "productos": listar_productos_select(),
        "solicitud": buscar_solicitud(id_solicitud),
    }

    if request.POST:

        cantidad = request.POST.get("cant")
        id_solicitud = request.POST.get("idsoli")
        id_producto = request.POST.get("cboproducto")

        salida = agregar_producto_detalle(cantidad, id_producto, id_solicitud)

        if salida == 1:
            messages.success(
                request,
                "La producto ha sido agregado correctamente.",
                extra_tags="alert alert-success",
            )
        else:
            messages.error(
                request,
                "Error al intentar agregar el producto.",
                extra_tags="alert alert-danger",
            )
        return redirect("listar_productos", id_solicitud)

    return render(request, "core/agregar_producto.html", data)


def agregar_producto_detalle(cantidad, id_producto, id_solicitud):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc(
        "SP_AGREGAR_PRODUCTO_DETALLE", [cantidad, id_producto, id_solicitud, salida]
    )
    return salida.getvalue()


@login_required
def formulario_solicitud(request):  # METODO PARA REALIZAR UNA SOLICITUD DE COMPRA

    if request.POST:

        fecha_pedido = datetime.datetime.now()
        direccion_destino = request.POST.get("direccion")
        fecha_min = request.POST.get("min")
        fecha_max = request.POST.get("max")
        id_usuario = request.user.id
        id_estado = 1

        salida = agregar_solicitud_compra(
            fecha_pedido, direccion_destino, id_estado, id_usuario, fecha_max, fecha_min
        )

        if salida == 1:
            messages.success(
                request,
                "Solicitud ingresada correctamente.",
                extra_tags="alert alert-success",
            )
        else:
            messages.error(
                request,
                "Error al intentar ingresar la solicitud.",
                extra_tags="alert alert-danger",
            )
        return redirect("solicitud_compra")

    return render(request, "core/formulario_solicitud.html")


def agregar_solicitud_compra(
    fecha_pedido, direccion_destino, id_estado, id_usuario, fecha_max, fecha_min
):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc(
        "SP_AGREGAR_SOLICITUD_COMPRA",
        [
            fecha_pedido,
            direccion_destino,
            id_estado,
            id_usuario,
            fecha_max,
            fecha_min,
            salida,
        ],
    )
    return salida.getvalue()


##################################################################################################
####                                                                                          ####
####                     FIN MODULO DE SOLICITUDES DE PROCESOS DE VENTA                       ####
####                                                                                          ####
##################################################################################################


##################################################################################################
####                                                                                          ####
####                       MODULO USUARIOS                                                    ####
####                                                                                          ####
##################################################################################################


@login_required
def modificar_datos_personales(
    request, id
):  # METODO PARA MODIFICAR LOS DATOS PERSONALES DEL USUARIO

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
def perfil_usuario(request, id):  # METODO PARA MOSTRAR EL PERFIL DEL USUARIO
    persona = PERSONA.objects.get(id_usuario=id)
    pais = PAIS.objects.all()

    return render(
        request, "core/perfil_usuario.html", {"persona": persona, "pais": pais}
    )


def registro_minorista(request):  # METODO DE REGISTRO DE USUARIO DE TIPO MINORISTA

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


def registro_usuario(
    request, cod
):  # METODO DE REGISTRO DE USUARIO MAYORISTA, PROVEEDOR Y TRANSPORTISTA

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


def buscar_persona(
    cod, rut, dni
):  # METODO PARA VER SI EXISTE LA PERSONA Y VERIFICAR EL CODIGO DE ACTIVACION

    persona = PERSONA()
    persona = (
        PERSONA.objects.filter(codigo_activacion=cod).filter(rut=rut).filter(dni=dni)
    )
    return persona


def codigo_activacion(
    request,
):  # METODO PARA BUSCAR LA PERSONA POR SU CODIGO DE ACTIVACION
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


##################################################################################################
####                                                                                          ####
####                       FIN MODULO DE USUARIO                                              ####
####                                                                                          ####
##################################################################################################
