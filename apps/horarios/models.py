from django.db import models
from apps.usuarios.models import Usuario
from apps.empresas.models import PuntosDeAcceso


# Create your models here.
class Horario(models.Model):
    punto_de_acceso = models.ForeignKey(PuntosDeAcceso, on_delete=models.CASCADE, related_name='horario')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='horario')
    hora_inicio = models.TimeField(blank=True, null=True)
    hora_fin = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.punto_de_acceso.nombre + ' ' + self.usuario.nombre + ' ' + self.usuario.apellido \
               + ' ' + self.hora_inicio.strftime('%H:%M') + ' ' + self.hora_fin.strftime('%H:%M')

    class Meta:
        db_table = 'grydd_horario'
