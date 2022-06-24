"""entrega1_nicotra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from futbol_app import views
from futbol_app.views import form_clubes, form_tecnicos, form_jugadores
from futbol_app.views import buscar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('futbol_app', views.inicio, name="Inicio"),
    path('form_jugadores', views.form_jugadores, name="Jugadores"),
    path('form_tecnicos', views.form_tecnicos, name="Tecnicos"),
    path('form_clubes', views.form_clubes, name="Clubes"),
    path('futbol_app/buscar/', views.buscar),

]
