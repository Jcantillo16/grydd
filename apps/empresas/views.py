from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Empresa, PuntosDeAcceso
from apps.usuarios.models import Usuario
from .serializers import EmpresaSerializer, PuntosDeAccesoSerializer


# Create your views here.
class EmpresaView(APIView):
    def get(self, request):
        usuario_admin = request.headers.get("usuario-id", None)
        if usuario_admin is None:
            return Response({"error": "este usuario administrador no existe"},
                            status=status.HTTP_400_BAD_REQUEST)
        usuario_admin = Usuario.objects.get(id=usuario_admin)
        if usuario_admin.role.nombre != "Administrador Del Sistema":
            return Response({"error": "No se puede crear una empresa sin ser administrador"},
                            status=status.HTTP_400_BAD_REQUEST)
        empresas = Empresa.objects.all()
        serializer = EmpresaSerializer(empresas, many=True)
        return Response(serializer.data)

    def post(self, request):
        usuario_admin = request.headers.get("usuario-id", None)
        if usuario_admin is None:
            return Response({"error": "este usuario administrador no existe"},
                            status=status.HTTP_400_BAD_REQUEST)
        usuario_admin = Usuario.objects.get(id=usuario_admin)
        if usuario_admin.role.nombre != "Administrador Del Sistema":
            return Response({"error": "No se puede crear una empresa sin ser administrador"},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = EmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmpresaDetail(APIView):
    def get(self, request, pk):
        usuario_admin = request.headers.get("usuario-id", None)
        if usuario_admin is None:
            return Response({"error": "este usuario administrador no existe"},
                            status=status.HTTP_400_BAD_REQUEST)
        usuario_admin = Usuario.objects.get(id=usuario_admin)
        if usuario_admin.role.nombre != "Administrador Del Sistema":
            return Response({"error": "solo puede consultar una empresa si es administrador"},
                            status=status.HTTP_400_BAD_REQUEST)
        empresa = Empresa.objects.get(id=pk)
        serializer = EmpresaSerializer(empresa)
        return Response(serializer.data)

    def put(self, request, pk):
        usuario_admin = request.headers.get("usuario-id", None)
        if usuario_admin is None:
            return Response({"error": "este usuario administrador no existe"},
                            status=status.HTTP_400_BAD_REQUEST)
        usuario_admin = Usuario.objects.get(id=usuario_admin)
        if usuario_admin.role.nombre != "Administrador Del Sistema":
            return Response({"error": "solo puede actualizar una empresa si es administrador"},
                            status=status.HTTP_400_BAD_REQUEST)
        empresa = Empresa.objects.get(id=pk)
        serializer = EmpresaSerializer(empresa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        usuario_admin = request.headers.get("usuario-id", None)
        if usuario_admin is None:
            return Response({"error": "este usuario administrador no existe"},
                            status=status.HTTP_400_BAD_REQUEST)
        usuario_admin = Usuario.objects.get(id=usuario_admin)
        if usuario_admin.role.nombre != "Administrador Del Sistema":
            return Response({"error": "solo puede eliminar una empresa si es administrador"},
                            status=status.HTTP_400_BAD_REQUEST)
        empresa = Empresa.objects.get(id=pk)
        empresa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PuntoDeAccesoView(APIView):
    def get(self, request):
        usuario_admin_empresa = request.headers.get("usuario-id", None)
        if usuario_admin_empresa is None:
            return Response({"error": "este usuario administrador  de empresa no existe"},
                            status=status.HTTP_400_BAD_REQUEST)
        usuario_admin_empresa = Usuario.objects.get(id=usuario_admin_empresa)
        if usuario_admin_empresa.role.nombre != "Administrador De La Empresa":
            return Response({"error": "solo puede consultar un punto de acceso si es administrador de la empresa"},
                            status=status.HTTP_400_BAD_REQUEST)
        puntos_de_acceso = PuntosDeAcceso.objects.all()
        serializer = PuntosDeAccesoSerializer(puntos_de_acceso, many=True)
        return Response(serializer.data)

    def post(self, request):
        usuario_admin_empresa = request.headers.get("usuario-id", None)
        if usuario_admin_empresa is None:
            return Response({"error": "este usuario administrador  de empresa no existe"},
                            status=status.HTTP_400_BAD_REQUEST)
        usuario_admin_empresa = Usuario.objects.get(id=usuario_admin_empresa)
        if usuario_admin_empresa.role.nombre != "Administrador De La Empresa":
            return Response({"error": "solo puede crear un punto de acceso si es administrador de la empresa"},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = PuntosDeAccesoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PuntoDeAccesoDetail(APIView):
    def get(self, request, pk):
        usuario_admin_empresa = request.headers.get("usuario-id", None)
        if usuario_admin_empresa is None:
            return Response({"error": "este usuario administrador  de empresa no existe"},
                            status=status.HTTP_400_BAD_REQUEST)
        usuario_admin_empresa = Usuario.objects.get(id=usuario_admin_empresa)
        if usuario_admin_empresa.role.nombre != "Administrador De La Empresa":
            return Response({"error": "solo puede consultar un punto de acceso si es administrador de la empresa"},
                            status=status.HTTP_400_BAD_REQUEST)
        punto_de_acceso = PuntosDeAcceso.objects.get(id=pk)
        serializer = PuntosDeAccesoSerializer(punto_de_acceso)
        return Response(serializer.data)

    def put(self, request, pk):
        usuario_admin_empresa = request.headers.get("usuario-id", None)
        if usuario_admin_empresa is None:
            return Response({"error": "este usuario administrador  de empresa no existe"},
                            status=status.HTTP_400_BAD_REQUEST)
        usuario_admin_empresa = Usuario.objects.get(id=usuario_admin_empresa)
        if usuario_admin_empresa.role.nombre != "Administrador De La Empresa":
            return Response({"error": "solo puede actualizar un punto de acceso si es administrador de la empresa"},
                            status=status.HTTP_400_BAD_REQUEST)
        punto_de_acceso = PuntosDeAcceso.objects.get(id=pk)
        serializer = PuntosDeAcces
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        usuario_admin_empresa = request.headers.get("usuario-id", None)
        if usuario_admin_empresa is None:
            return Response({"error": "este usuario administrador  de empresa no existe"},
                            status=status.HTTP_400_BAD_REQUEST)
        usuario_admin_empresa = Usuario.objects.get(id=usuario_admin_empresa)
        if usuario_admin_empresa.role.nombre != "Administrador De La Empresa":
            return Response({"error": "solo puede eliminar un punto de acceso si es administrador de la empresa"},
                            status=status.HTTP_400_BAD_REQUEST)
        punto_de_acceso = PuntosDeAcceso.objects.get(id=pk)
        punto_de_acceso.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
