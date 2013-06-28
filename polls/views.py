from django.http import HttpResponse
from django.template import Context, loader
from polls import models

def index(request):
    lista_personas = models.Poll.objects.all()
    tmpl = loader.get_template("index.html")
    contexto = Context({'valor': lista_personas})
    return HttpResponse(tmpl.render(contexto))