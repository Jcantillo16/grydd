from rest_framework import serializers
from .models import Horario


class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = '__all__'

    def to_representation(self, instance):
        ret = super(HorarioSerializer, self).to_representation(instance)
        ret['ciudad'] = instance.punto_de_acceso.ciudad + ', ' + instance.punto_de_acceso.nombre
        ret['usuario'] = instance.usuario.nombre + ' ' + instance.usuario.apellido
        return ret
