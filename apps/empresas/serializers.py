from rest_framework import serializers
from .models import Empresa, PuntosDeAcceso
from apps.horarios.serializers import HorarioSerializer


class PuntosDeAccesoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PuntosDeAcceso
        fields = '__all__'

    def validate(self, data):
        if data['ciudad'] == 'Bogota':
            data['geolocalizacion'] = '4.63701,-74.08406'
            return data
        elif data['ciudad'] == 'Cali':
            data['geolocalizacion'] = '3.45, -76.5'
            return data
        elif data['ciudad'] == 'Medellin':
            data['geolocalizacion'] = '6.25, -75.56'
            return data
        elif data['ciudad'] == 'Barranquilla':
            data['geolocalizacion'] = '10.9, -74.8'
            return data
        elif data['ciudad'] == 'Bucaramanga':
            data['geolocalizacion'] = '7.13, -73.12'
            return data
        else:
            raise serializers.ValidationError('Empresa No tiene Puntos de Acceso en esta Ciudad')


class EmpresaSerializer(serializers.ModelSerializer):
    puntos_de_acceso = PuntosDeAccesoSerializer(read_only=True, many=True)
    class Meta:
        model = Empresa
        fields = '__all__'

    def to_representation(self, instance):
        ret = super(EmpresaSerializer, self).to_representation(instance)
        ret['usuario_admin'] = instance.usuario_admin.nombre + ' ' + instance.usuario_admin.apellido
        return ret

    def validate(self, data):
        if data['usuario_admin'].role.nombre != 'Administrador Del Sistema':
            raise serializers.ValidationError('El usuario debe ser administrador del sistema')
        return data
