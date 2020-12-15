from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .form import RegisterForm, ReservaForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import *
# Create your views here.
# rodar o serve (python manage.py runserver)
def index(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy("reservar"))
    return render(request, 'index.html')
    

def registrar(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("/login")
    return render(request, 'registrar.html', context={"form": form})

@login_required(login_url='/login/')
def reservar(request):
    form = ReservaForm()
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save()
            reserva.professor = request.user
            reserva.save()
            form = ReservaForm()
            return redirect(reverse_lazy('pedido-confirmado'))
          
    return render(request, 'reservar.html', context={"form": form})

def reservas(request):
    context = {
        "reservas": Reserva.objects.all()
    }
    return render(request, 'reservas.html', context)

@login_required(login_url='/login/')
def pedido(request):
    return render(request, 'pedido-confirmado.html')

