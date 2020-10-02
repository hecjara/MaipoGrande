from django.urls import path
from .views import home, registro_minorista, codigo_activacion, registro_usuario, links, solicitud_compra, formulario_solicitud, listar_productos, agregar_producto

urlpatterns = [
    path('', home, name="home"),
    path('registro_minorista/', registro_minorista, name='registro_minorista'),
    path('codigo_activacion/', codigo_activacion, name="codigo_activacion"),
    path('registro_usuario/<cod>/', registro_usuario, name="registro_usuario"),
    path('links/', links, name="links"),
    path('solicitud_compra/', solicitud_compra, name="solicitud_compra"),
    path('formulario_solicitud/', formulario_solicitud, name="formulario_solicitud"),
    path('agregar_producto/<id>/', agregar_producto, name="agregar_producto"),
    path('listar_productos/<id>/', listar_productos, name="listar_productos"),
]
