from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from futbol_app.models import Jugador, Tecnico, Club
from futbol_app.forms import Form_Jugador, Form_Tecnico, Form_Club

# Create your views here.

def inicio(request):

    return render(request, "futbol_app/inicio.html")

def jugadores(request):

    return render(request, "futbol_app/form_jugadores.html")

def form_jugadores(request):

    if request.method == 'POST':
        mi_formulario = Form_Jugador(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid:
            informacion = mi_formulario.cleaned_data

            jugador = Jugador(apellido=informacion['apellido'], camiseta=informacion['camiseta'])
            jugador.save()
            return render(request, 'futbol_app/inicio.html')
    
    else:
        mi_formulario = Form_Jugador()
    
    return render(request, 'futbol_app/form_jugadores.html', {'mi_formulario':mi_formulario})

def tecnicos(request):

    return render(request, "futbol_app/form_tecnicos.html")

def form_tecnicos(request):

    if request.method == 'POST':
        mi_formulario = Form_Tecnico(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid:
            informacion = mi_formulario.cleaned_data

            tecnico = Tecnico(nombre=informacion['nombre'], apellido=informacion['apellido'], club=informacion['club'])
            tecnico.save()
            return render(request, 'futbol_app/inicio.html')
    
    else:
        mi_formulario = Form_Tecnico()
    
    return render(request, 'futbol_app/form_tecnicos.html', {'mi_formulario':mi_formulario})

def clubes(request):

    return render(request, "futbol_app/form_clubes.html")

def form_clubes(request):

    if request.method == 'POST':
        mi_formulario = Form_Club(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid:
            informacion = mi_formulario.cleaned_data

            club = Club(club=informacion['club'], ligas=informacion['ligas'], descensos=informacion['descensos'])
            club.save()
            return render(request, 'futbol_app/inicio.html')
    
    else:
        mi_formulario = Form_Club()
    
    return render(request, 'futbol_app/form_clubes.html', {'mi_formulario':mi_formulario})


def buscar(request):
    if request.GET['camiseta']:
        camiseta = request.GET['camiseta']
        print(camiseta)
        jugador = Jugador.objects.filter(camiseta__icontains=camiseta)
        print(jugador)
        return render(request, 'futbol_app/buscar_jugador.html', {'jugadores':jugador, 'camiseta':camiseta})
    else:
        respuesta = "No enviaste datos"
    return render(request, 'futbol_app/inicio.html', {'respuesta':respuesta})


    
    





