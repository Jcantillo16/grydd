from django.urls import path
from .registro import Registro
from .views import CrearUsuarios, UsuarioDetail

urlpatterns = [
    path('registro/', Registro.as_view(), name='registro'),
    path('crear_usuario/', CrearUsuarios.as_view(), name='crear_usuario'),
    path('usuario/<int:pk>/', UsuarioDetail.as_view(), name='usuario'),

]
