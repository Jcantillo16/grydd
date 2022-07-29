from django.urls import path
from .views import EmpresaView, EmpresaDetail, PuntoDeAccesoView, PuntoDeAccesoDetail

urlpatterns = [
    path('empresas/', EmpresaView.as_view(), name='empresa'),
    path('empresas/<int:pk>/', EmpresaDetail.as_view(), name='empresa-detail'),
    path('punto-de-acceso/', PuntoDeAccesoView.as_view(), name='punto-de-acceso'),
    path('punto-de-acceso/<int:pk>/', PuntoDeAccesoDetail.as_view(), name='punto-de-acceso-detail'),
]
