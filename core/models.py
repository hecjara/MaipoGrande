from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PAIS(models.Model):
    id_pais = models.AutoField(primary_key=True)
    iso = models.CharField(max_length=2, null=False, blank=False)
    nombre_pais = models.CharField(max_length=50, null=False, blank=False)

    def __getitem__(self, index):
        """Return the form at the given index, based on the rendering order."""
        return self.forms[index]

    def __str__(self):
        return u"{0}".format(self.nombre_pais)


class EMPRESA(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField(max_length=50, null=False, blank=False)
    contacto = models.IntegerField(null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)
    id_pais = models.ForeignKey(PAIS, on_delete=models.CASCADE)


class TIPO_CONTRATO(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    nombre_tipo = models.CharField(max_length=50, null=False, blank=False)


class ESTADO_CONTRATO(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nombre_estado = models.CharField(max_length=50, null=False, blank=False)


class TIPO_PERSONA(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    nombre_tipo = models.CharField(max_length=50, null=False, blank=False)


class PERSONA(models.Model):
    id_persona = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=11, null=True, blank=True)
    dni = models.CharField(max_length=20, null=True, blank=True)
    nombres = models.CharField(max_length=100, null=False, blank=False)
    apellidos = models.CharField(max_length=100, null=False, blank=False)
    fecha_nacimiento = models.DateField(null=False, blank=False)
    telefono = models.IntegerField(null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)
    direccion = models.CharField(max_length=100, null=False, blank=False)
    id_empresa = models.OneToOneField(
        EMPRESA, on_delete=models.CASCADE, null=True, blank=True
    )
    id_usuario = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    id_pais = models.ForeignKey(PAIS, on_delete=models.CASCADE, null=True, blank=True)
    codigo_activacion = models.IntegerField(null=True, blank=True)
    id_tipo = models.ForeignKey(
        TIPO_PERSONA, on_delete=models.CASCADE, null=True, blank=True
    )


class CONTRATO(models.Model):
    id_contrato = models.AutoField(primary_key=True)
    contrato = models.TextField(null=False, blank=False)
    fecha_inicio = models.DateField(null=False, blank=False)
    fecha_termino = models.DateField(null=False, blank=False)
    fecha_actualizacion = models.DateField(null=False, blank=False)
    id_tipo = models.ForeignKey(TIPO_CONTRATO, on_delete=models.CASCADE)
    id_estado = models.ForeignKey(
        ESTADO_CONTRATO, on_delete=models.CASCADE
    )  # cascade = si borro un id_estado, se borraran todas las contratos asociadas
    id_persona = models.ForeignKey(PERSONA, on_delete=models.CASCADE)


class ASEGURADORA(models.Model):
    id_aseguradora = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    telefono = models.IntegerField(null=False, blank=False)
    direccion = models.CharField(max_length=100, null=False, blank=False)
    id_pais = models.ForeignKey(PAIS, on_delete=models.CASCADE)


class ESTADO_POLIZA(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nombre_estado = models.CharField(max_length=30, null=False, blank=False)


class SEGURO(models.Model):
    id_seguro = models.AutoField(primary_key=True)
    poliza = models.CharField(max_length=35, null=False, blank=False)
    fecha_actualizacion = models.DateField(null=False, blank=False)
    id_persona = models.ForeignKey(
        PERSONA, on_delete=models.CASCADE, null=True, blank=True
    )
    id_aseguradora = models.ForeignKey(ASEGURADORA, on_delete=models.CASCADE)
    id_estado = models.ForeignKey(ESTADO_POLIZA, on_delete=models.CASCADE)


class FORMA_PAGO(models.Model):
    id_forma = models.AutoField(primary_key=True)
    nombre_forma = models.CharField(max_length=30, null=False, blank=False)


class BANCO(models.Model):
    id_banco = models.AutoField(primary_key=True)
    nombre_banco = models.CharField(max_length=100, null=False, blank=False)


class DATO_PAGO(models.Model):
    id_forma = models.AutoField(primary_key=True)
    cuenta_corriente = models.CharField(max_length=30, null=False, blank=False)
    id_persona = models.ForeignKey(PERSONA, on_delete=models.CASCADE)
    id_forma = models.ForeignKey(FORMA_PAGO, on_delete=models.CASCADE)
    id_banco = models.ForeignKey(BANCO, on_delete=models.CASCADE)


class ESTADO_SUBASTA(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nombre_estado = models.CharField(max_length=50, null=False, blank=False)


class TRANSPORTE(models.Model):
    id_transporte = models.AutoField(primary_key=True)
    refrigeracion = models.CharField(max_length=2, null=False, blank=False)
    tamanio = models.CharField(max_length=30, null=False, blank=False)
    capacidad_carga = models.FloatField(null=False, blank=False)
    direccion_origen = models.CharField(max_length=100, null=False, blank=False)
    fecha_entrega = models.DateField(null=False, blank=False)
    adicional = models.TextField(null=True, blank=True)


class ESTADO_SOLICITUD(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nombre_estado = models.CharField(max_length=50, null=False, blank=False)


class SOLICITUD_COMPRA(models.Model):
    id_solicitud = models.AutoField(primary_key=True)
    fecha_pedido = models.DateField(null=False, blank=False)
    direccion_destino = models.CharField(max_length=100, null=False, blank=False)
    fecha_min = models.DateField(null=False, blank=False)
    fecha_max = models.DateField(null=False, blank=False)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    id_estado = models.ForeignKey(ESTADO_SOLICITUD, on_delete=models.CASCADE)


class PRODUCTO(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    imagen = models.CharField(null=True, blank=True, max_length=300)


class BODEGA(models.Model):
    id_bodega = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    direccion = models.CharField(max_length=50, null=False, blank=False)


class DETALLE_SOLICITUD(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(PRODUCTO, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=False, blank=False)
    id_solicitud = models.ForeignKey(SOLICITUD_COMPRA, on_delete=models.CASCADE)


class ESTADO_PROD_BOD(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)


class PRODUCTO_BODEGA(models.Model):
    id_prod_bod = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(PRODUCTO, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=False, blank=False)
    precio_kilo = models.IntegerField(null=False, blank=False)
    fecha_elaboracion = models.DateField(null=False, blank=False)
    fecha_vencimiento = models.DateField(null=False, blank=False)
    id_estado = models.ForeignKey(ESTADO_PROD_BOD, on_delete=models.CASCADE)
    id_bodega = models.ForeignKey(BODEGA, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)


class ESTADO_PROCESO_VENTA(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nombre_estado = models.CharField(max_length=50, null=False, blank=False)


class PROCESO_VENTA(models.Model):
    id_proceso = models.AutoField(primary_key=True)
    fecha_inicio = models.DateTimeField(null=False, blank=False)
    fecha_termino = models.DateTimeField(null=False, blank=False)
    id_solicitud = models.ForeignKey(
        SOLICITUD_COMPRA, on_delete=models.CASCADE, null=True, blank=True
    )
    id_estado = models.ForeignKey(ESTADO_PROCESO_VENTA, on_delete=models.CASCADE)


class CONCLUSION(models.Model):
    id_conclusion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)


class HISTORIAL_POSTULACION(models.Model):
    id_historial = models.AutoField(primary_key=True)
    oferta = models.IntegerField(null=False, blank=False)
    cantidad = models.IntegerField(null=False, blank=False)
    fecha_oferta = models.DateTimeField(null=False, blank=False)
    id_proceso = models.ForeignKey(PROCESO_VENTA, on_delete=models.CASCADE)
    id_prod_bod = models.ForeignKey(PRODUCTO_BODEGA, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    id_conclusion = models.ForeignKey(
        CONCLUSION, on_delete=models.CASCADE, null=True, blank=True
    )


class SUBASTA_TRANSPORTE(models.Model):
    id_subasta = models.AutoField(primary_key=True)
    fecha_inicio = models.DateTimeField(null=False, blank=False)
    fecha_termino = models.DateTimeField(null=False, blank=False)
    id_proceso = models.OneToOneField(PROCESO_VENTA, on_delete=models.CASCADE)
    id_estado = models.ForeignKey(ESTADO_SUBASTA, on_delete=models.CASCADE)
    id_transporte = models.ForeignKey(TRANSPORTE, on_delete=models.CASCADE)


# class HISTORiAL_SUBASTA(models.Model):
#     id_historial = models.AutoField(primary_key=True)
#     oferta = models.IntegerField(null=False, blank=False)
#     fecha_oferta = models.DateTimeField(null=False, blank=False)
#     id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
#     id_subasta = models.ForeignKey(SUBASTA_TRANSPORTE, on_delete=models.CASCADE)

class HISTORIAL_SUBASTA(models.Model):
    id_historial = models.AutoField(primary_key=True)
    oferta = models.IntegerField(null=False, blank=False)
    fecha_oferta = models.DateTimeField()
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    id_subasta = models.ForeignKey(SUBASTA_TRANSPORTE, on_delete=models.CASCADE)


class TIPO_PAGO(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    nombre_tipo = models.CharField(max_length=50, null=False, blank=False)


class ESTADO_MINORISTA(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)


class PROCESO_MINORISTA(models.Model):
    id_proceso = models.AutoField(primary_key=True)
    fecha_inicio = models.DateTimeField(null=False, blank=False)
    fecha_termino = models.DateTimeField(null=False, blank=False)
    id_prod_bod = models.ForeignKey(PRODUCTO_BODEGA, on_delete=models.CASCADE)
    id_estado = models.ForeignKey(
        ESTADO_MINORISTA, on_delete=models.CASCADE, null=True, blank=True
    )


class PAGO(models.Model):
    id_pago = models.AutoField(primary_key=True)
    total = models.IntegerField(null=False, blank=False)
    fecha_pago = models.DateTimeField(null=False, blank=False)
    id_tipo = models.ForeignKey(TIPO_PAGO, on_delete=models.CASCADE)
    id_dato_pago = models.ForeignKey(DATO_PAGO, on_delete=models.CASCADE)
    id_proceso = models.ForeignKey(
        PROCESO_VENTA, on_delete=models.CASCADE, null=True, blank=True
    )
    id_proceso_mino = models.ForeignKey(
        PROCESO_MINORISTA, on_delete=models.CASCADE, null=True, blank=True
    )

