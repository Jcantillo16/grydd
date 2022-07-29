from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Horario
from .serializers import HorarioSerializer
from apps.usuarios.models import Usuario


class HorarioView(APIView):
    def get(self, request):
        usuario_admin = request.headers.get("usuario-id", None)
        if usuario_admin is None:
            return Response({"error": "este usuario administrador de empresa no existe"},
                            status=status.HTTP_400_BAD_REQUEST)
        usuario_admin = Usuario.objects.get(id=usuario_admin)
        if usuario_admin.role.nombre != "Administrador De La Empresa":
            return Response({"error": "No se puede consultar los horario sin ser administrador de empresa"},
                            status=status.HTTP_400_BAD_REQUEST)
        horarios = Horario.objects.all()
        serializer = HorarioSerializer(horarios, many=True)
        return Response(serializer.data)

    def post(self, request):
        usuario_admin = request.headers.get("usuario-id", None)
        if usuario_admin is None:
            return Response({"error": "este usuario administrador de empresa no existe"},
                            status=status.HTTP_400_BAD_REQUEST)
        usuario_admin = Usuario.objects.get(id=usuario_admin)
        if usuario_admin.role.nombre != "Administrador De La Empresa":
            return Response({"error": "No se puede crear un horario sin ser administrador de empresa"},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = HorarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HorarioDetail(APIView):
    def get(self, request, pk):
        usuario_admin = request.headers.get("usuario-id", None)
        if usuario_admin is None:
            return Response({"error": "este usuario administrador de empresa no existe"},
                            status=status.HTTP_400_BAD_REQUEST)
        usuario_admin = Usuario.objects.get(id=usuario_admin)
        if usuario_admin.role.nombre != "Administrador De La Empresa":
            return Response({"error": "solo puede consultar un horario si es administrador de empresa"},
                            status=status.HTTP_400_BAD_REQUEST)
        horario = Horario.objects.get(id=pk)
        serializer = HorarioSerializer(horario)
        return Response(serializer.data)

    def put(self, request, pk):
        usuario_admin = request.headers.get("usuario-id", None)
        if usuario_admin is None:
            return Response({"error": "este usuario administrador de empresa no existe"},
                            status=status.HTTP_400_BAD_REQUEST)
        usuario_admin = Usuario.objects.get(id=usuario_admin)
        if usuario_admin.role.nombre != "Administrador De La Empresa":
            return Response({"error": "solo puede actualizar un horario si es administrador de empresa"},
                            status=status.HTTP_400_BAD_REQUEST)
        horario = Horario.objects.get(id=pk)
        serializer = HorarioSerializer(horario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        usuario_admin = request.headers.get("usuario-id", None)
        if usuario_admin is None:
            return Response({"error": "este usuario administrador de empresa no existe"},
                            status=status.HTTP_400_BAD_REQUEST)
        usuario_admin = Usuario.objects.get(id=usuario_admin)
        if usuario_admin.role.nombre != "Administrador De La Empresa":
            return Response({"error": "solo puede eliminar  un horario si es administrador de empresa"},
                            status=status.HTTP_400_BAD_REQUEST)
        horario = Horario.objects.get(id=pk)
        horario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

