from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UsuarioSerializer
from .models import Usuario, Role
from .registro import Registro
from django.conf import settings
from django.core.mail import send_mail


class CrearUsuarios(APIView):
    # enviar correo a usuario creado
    def post(self, request):
        admin = request.headers.get("usuario-id", None)
        if admin is None:
            return Response({"error": "No se puede crear un usuario sin ser administrador"},
                            status=status.HTTP_400_BAD_REQUEST)
        admin = Usuario.objects.get(id=admin)
        if admin.role.nombre != "Administrador Del Sistema":
            return Response({"error": "No se puede crear un usuario sin ser administrador"},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_mail(
                'Bienvenido a Grydd',
                'Hola ' + serializer.data['nombre'] + ' ' + serializer.data['apellido'] + '\n' + 'Bienvenido a Grydd',
                serializer.data['email'],
                [serializer.data['email']],
                fail_silently=False,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        admin = request.headers.get("usuario-id", None)
        if admin is None:
            return Response({"error": "No se puede consultar un usuario sin ser administrador"},
                            status=status.HTTP_400_BAD_REQUEST)
        admin = Usuario.objects.get(id=admin)
        if admin.role.nombre != "Administrador Del Sistema":
            return Response({"error": "No se puede consultar un usuario sin ser administrador"},
                            status=status.HTTP_400_BAD_REQUEST)
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)


class UsuarioDetail(APIView):
    def get(self, request, pk):
        admin = request.headers.get("usuario-id", None)
        if admin is None:
            return Response({"error": "No se puede consultar un usuario sin ser administrador"},
                            status=status.HTTP_400_BAD_REQUEST)
        admin = Usuario.objects.get(id=admin)
        if admin.role.nombre != "Administrador Del Sistema":
            return Response({"error": "No se puede consultar un usuario sin ser administrador"},
                            status=status.HTTP_400_BAD_REQUEST)
        usuario = Usuario.objects.get(id=pk)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    def put(self, request, pk):
        admin = request.headers.get("usuario-id", None)
        if admin is None:
            return Response({"error": "No se puede actualizar un usuario sin ser administrador"},
                            status=status.HTTP_400_BAD_REQUEST)
        admin = Usuario.objects.get(id=admin)
        if admin.role.nombre != "Administrador Del Sistema":
            return Response({"error": "No se puede actualizar un usuario sin ser administrador"},
                            status=status.HTTP_400_BAD_REQUEST)
        usuario = Usuario.objects.get(id=pk)
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        admin = request.headers.get("usuario-id", None)
        if admin is None:
            return Response({"error": "No se puede eliminar un usuario sin ser administrador"},
                            status=status.HTTP_400_BAD_REQUEST)
        admin = Usuario.objects.get(id=admin)
        if admin.role.nombre != "Administrador Del Sistema":
            return Response({"error": "No se puede eliminar un usuario sin ser administrador"},
                            status=status.HTTP_400_BAD_REQUEST)
        usuario = Usuario.objects.get(id=pk)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
