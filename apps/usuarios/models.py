from django.db import models


# Create your models here.
class Role(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'grydd_role'


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    empresa = models.ForeignKey('empresas.Empresa', on_delete=models.CASCADE, related_name='usuario', null=True,
                                blank=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True, null=False, blank=False)
    indicativo_telefono = models.CharField(max_length=100, default='+57', blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre + ' ' + self.apellido

    class Meta:
        db_table = 'grydd_usuario'


