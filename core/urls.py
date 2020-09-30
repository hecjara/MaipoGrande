from django.urls import path
from .views import home, registro_minorista, codigo_activacion, registro_usuario, links, solicitud_compra

urlpatterns = [
    path('', home, name="home"),
    path('registro_minorista/', registro_minorista, name='registro_minorista'),
    path('codigo_activacion/', codigo_activacion, name="codigo_activacion"),
    path('registro_usuario/<cod>/', registro_usuario, name="registro_usuario"),
    path('links/', links, name="links"),
    path('solicitud_compra/', solicitud_compra, name="solicitud_compra"),
]
