from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import Context, loader
from polls import models
from polls.models import Producto

def index(request):
    lista_personas = models.Producto.objects.all()
    tmpl = loader.get_template("index.html")
    contexto = Context({'valor': lista_personas})
    return HttpResponse(tmpl.render(contexto))

def producto_view(request):
    prod = Producto.objects.filter(Precio=125000)
    ctx = {'productos':prod}
    return render_to_response('productos.html',ctx,context_instance=RequestContext(request))




