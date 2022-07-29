from django.db import models
from apps.usuarios.models import Usuario


# Create your models here.
class Empresa(models.Model):
    usuario_admin = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='empresa_admin')
    nombre = models.CharField(max_length=100)
    nit = models.CharField(max_length=100)
    nombre_comercial = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True, null=False, blank=False)
    indicativo_telefono = models.CharField(max_length=100, default='+57', blank=True, null=True)
    ciudad = models.CharField(max_length=100)
    sitio_web = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre_comercial + ' ' + self.sitio_web

    class Meta:
        db_table = 'grydd_empresa'


class PuntosDeAcceso(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='puntos_de_acceso', null=True,
                                blank=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True, null=False, blank=False)
    geolocalizacion = models.CharField(max_length=100, blank=True, null=True)
    ciudad = models.CharField(max_length=100)
    horarios_de_acceso = models.ForeignKey('horarios.Horario', on_delete=models.CASCADE,
                                           related_name='puntos_de_acceso', null=True, blank=True)

    def __str__(self):
        return self.nombre + ' ' + self.direccion

    class Meta:
        db_table = 'grydd_puntos_de_acceso'

    #validar que el usuario tenga rol de administrador de empresas.
    def save(self, *args, **kwargs):
        if self.empresa.usuario_admin.role.nombre != 'Administrador De La Empresa':
            raise serializers.ValidationError('El usuario debe ser Administrador De La Empresa')
        super(PuntosDeAcceso, self).save(*args, **kwargs)
