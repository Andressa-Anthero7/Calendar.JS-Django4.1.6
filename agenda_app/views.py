from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import requires_csrf_token

from .models import Agendamento


# Create your views here.


def index(request):
    agendamentos = Agendamento.objects.all()
    return render(request, 'agenda/index.html', {'agendamentos': agendamentos})


def criar_agendamento(request):
    if request.method == 'POST':
        titulo = request.POST.get('title')
        data = request.POST.get('hora')
        Agendamento.objects.create(
            title=titulo,
            data=data
        )
        return render(request, 'agenda/index.html')
    else:
        return render(request, 'agenda/index.html')


def editar_agendamento(request, pk):
    if request.method == 'POST':
        titulo = request.POST.get('title')
        data = request.POST.get('hora')
        Agendamento.objects.filter(pk=pk).update(
            title=titulo,
            data=data
        )
        return render(request, 'agenda/index.html')
    else:
        return render(request, 'agenda/index.html')


def deletar_agendamento(request, pk):
    deletar = get_object_or_404(Agendamento, pk=pk)
    deletar.delete()
    return render(request, 'agenda/index.html')

