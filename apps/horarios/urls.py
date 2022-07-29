from django.urls import path
from .views import HorarioView, HorarioDetail

urlpatterns = [
    path('horarios/', HorarioView.as_view(), name='horario'),
    path('horarios/<int:pk>/', HorarioDetail.as_view(), name='horario-detail'),
]
