from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from personas.models import Persona

# Create your views here.
#

#recibiendo id para trabajar cada persona
def detalle_persona(request, id):
    #recuperando el id, pk= primary key y evitando el error 404
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'personas/detalle.html', {'persona': persona})


#clase de django  para nuevo objeto para relacionar objeto formulario con modelo persona, este carga la variable con toda la informacion html
#te da la opcion para excluir algun campo del formulario, si no excluyes ninguno se hace de la siguiente forma:
PersonaForm = modelform_factory(Persona, exclude=[])

def nuevaPersona(request):
    formaPersona = PersonaForm()
    print(formaPersona)
    return render(request, 'personas/nuevo.html', {'formulario_persona':formaPersona})



