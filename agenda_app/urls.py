from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agendar/', views.criar_agendamento, name='cria_agendamento'),
    path('editar/<int:pk>/', views.editar_agendamento, name='editar_agendamento'),
    path('deletar/<int:pk>/', views.deletar_agendamento, name='deletar_agendamento')

]