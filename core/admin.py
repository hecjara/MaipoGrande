from django.contrib import admin
from .models import ASEGURADORA, BODEGA, CONTRATO, DATO_PAGO, DETALLE_SOLICITUD, EMPRESA, ESTADO_CONTRATO, ESTADO_POLIZA, ESTADO_PROCESO_VENTA, ESTADO_SOLICITUD, ESTADO_SUBASTA, FORMA_PAGO, HISTORiAL_SUBASTA, PAGO, PAIS, PERSONA, POSTULACION_PRODUCTO, PROCESO_VENTA, PRODUCTO, SEGURO, SOLICITUD_COMPRA, SUBASTA_TRANSPORTE, TIPO_CONTRATO, TIPO_PAGO, TIPO_PROCESO_VENTA, TRANSPORTE 

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id_producto', 'nombre', 'imagen']
    search_fields = ['nombre']
    list_filter = ['nombre']
    list_per_page = 10


admin.site.register(ASEGURADORA)
admin.site.register(BODEGA)
admin.site.register(CONTRATO)
admin.site.register(DATO_PAGO)
admin.site.register(DETALLE_SOLICITUD)
admin.site.register(EMPRESA)
admin.site.register(ESTADO_CONTRATO)
admin.site.register(ESTADO_POLIZA)
admin.site.register(ESTADO_PROCESO_VENTA)
admin.site.register(ESTADO_SOLICITUD)
admin.site.register(ESTADO_SUBASTA)
admin.site.register(FORMA_PAGO)
admin.site.register(HISTORiAL_SUBASTA)
admin.site.register(PAGO)
admin.site.register(PAIS)
admin.site.register(PERSONA)
admin.site.register(POSTULACION_PRODUCTO)
admin.site.register(PROCESO_VENTA)
admin.site.register(PRODUCTO, ProductoAdmin)
admin.site.register(SEGURO)
admin.site.register(SOLICITUD_COMPRA)
admin.site.register(SUBASTA_TRANSPORTE)
admin.site.register(TIPO_CONTRATO)
admin.site.register(TIPO_PAGO)
admin.site.register(TIPO_PROCESO_VENTA)
admin.site.register(TRANSPORTE)
