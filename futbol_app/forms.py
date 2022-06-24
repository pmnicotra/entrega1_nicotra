from django import forms

class Form_Jugador(forms.Form):
    apellido = forms.CharField(max_length=20)
    camiseta = forms.IntegerField()

class Form_Tecnico(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    club = forms.CharField(max_length=20)

class Form_Club(forms.Form):
    club = forms.CharField(max_length=20)
    ligas = forms.IntegerField()
    descensos = forms.BooleanField()



