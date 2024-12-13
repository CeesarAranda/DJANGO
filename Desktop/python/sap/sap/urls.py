
from django.contrib import admin
from django.urls import path
from webapp.views import bienvenido
from personas.views import detalle_persona, nuevaPersona

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenido),
    # los <> son para recibir parametros, que parametro va a recibir es un entero ya que es un id
    path('detalle_persona/<int:id>', detalle_persona),
    path('nueva_persona', nuevaPersona),
]
