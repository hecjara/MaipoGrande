from django.urls import path
from .views import (
    home,
    registro_minorista,
    codigo_activacion,
    registro_usuario,
    solicitud_compra,
    formulario_solicitud,
    listar_productos,
    agregar_producto,
    anular_solicitud,
    modificar_datos_personales,
    perfil_usuario,
    eliminar_detalleproducto,
    modificar_detalleproducto,
    listar_procesoventa,
)

urlpatterns = [
    path("", home, name="home"),
    path("registro_minorista/", registro_minorista, name="registro_minorista"),
    path("codigo_activacion/", codigo_activacion, name="codigo_activacion"),
    path("registro_usuario/<cod>/", registro_usuario, name="registro_usuario"),
    path("solicitud_compra/", solicitud_compra, name="solicitud_compra"),
    path("formulario_solicitud/", formulario_solicitud, name="formulario_solicitud"),
    path("agregar_producto/<id>/", agregar_producto, name="agregar_producto"),
    path("listar_productos/<id>/", listar_productos, name="listar_productos"),
    path("anular_solicitud/<id>/", anular_solicitud, name="anular_solicitud"),
    path("perfil_usuario/<id>/", perfil_usuario, name="perfil_usuario"),
    path("modificar_datos_personales/<id>/", modificar_datos_personales, name="modificar_datos_personales"),
    path("eliminar_detalleproducto/<id>/", eliminar_detalleproducto, name="eliminar_detalleproducto"),
    path("modificar_detalleproducto/<id>/", modificar_detalleproducto, name="modificar_detalleproducto"),
    path("listar_procesoventa/", listar_procesoventa, name="listar_procesoventa"),
]
