from rest_framework import serializers
from .models import Usuario, Role
from apps.empresas.serializers import EmpresaSerializer
from apps.horarios.serializers import HorarioSerializer



class UsuarioSerializer(serializers.ModelSerializer):
    empresa_admin = EmpresaSerializer(read_only=True, many=True)
    # horario = HorarioSerializer(read_only=True, many=True)

    class Meta():
        model = Usuario
        fields = '__all__'

    def create(self, validated_data):
        indicativo_telefono = validated_data.get('indicativo_telefono')
        if indicativo_telefono == '+57':
            validated_data['pais'] = 'Colombia'
        elif indicativo_telefono == '+1':
            validated_data['pais'] = 'Estados Unidos'
        elif indicativo_telefono == '+52':
            validated_data['pais'] = 'México'
        elif indicativo_telefono == '+55':
            validated_data['pais'] = 'Brasil'
        elif indicativo_telefono == '+1':
            validated_data['pais'] = 'Estados Unidos'
        else:
            validated_data['pais'] = 'Otro'
        return super(UsuarioSerializer, self).create(validated_data)

    def to_representation(self, instance):
        ret = super(UsuarioSerializer, self).to_representation(instance)
        ret['role'] = instance.role.nombre
        if instance.role.nombre == 'Empleado':
            ret['horario'] = HorarioSerializer(instance.horario, many=True).data
        return ret

    def validate(self, data):
        if data['role'].nombre == 'Administrador Del Sistema':
            if Usuario.objects.filter(role__nombre='Administrador Del Sistema').exists():
                raise serializers.ValidationError('Solo puede existir un usuario con el rol de admin')
        return data


