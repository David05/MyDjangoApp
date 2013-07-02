from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import Context, loader
from polls import models
from polls.models import Producto
from polls.forms import ClienteForm
from django.core.mail import EmailMultiAlternatives
from polls.forms import addProductos
from polls.models import prueba


def add_producto_view(request):
    if request.method=="POST":
        form = addProductos(request.POST)
        info = "Inicializado"
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            descripcion = form.cleaned_data['descripcion']
            p= prueba()
            p.nombre = nombre
            p.Descripcion = descripcion
            p.save() #Guardo la info
            info = "Se guardo los datos correctamente"
        else:  #no es valida
            info = "Informacion con datos erroneos"
        form = addProductos()
        ctx = {'form':form,'informacion':info }
        return render_to_response('addProducto.html',ctx, context_instance=RequestContext(request))
    else: #GET
        form = addProductos
        ctx = {'form':form}
        return render_to_response('addProducto.html',ctx, context_instance=RequestContext(request))

def index(request):
    lista_personas = models.Producto.objects.all()
    tmpl = loader.get_template("index.html")
    contexto = Context({'valor': lista_personas})
    return HttpResponse(tmpl.render(contexto))

def producto_view(request):
    prod = Producto.objects.filter(Precio=125000)
    ctx = {'productos':prod}
    return render_to_response('productos.html',ctx,context_instance=RequestContext(request))

def menu_view(request):
    return render_to_response('base.html',context_instance=RequestContext(request))

def Contatcto_view(request):
    info_envianda = False
    email = ""
    titulo = ""
    texto =""

    if request.method == "POST":
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            info_envianda = True
            email = formulario.cleaned_data['Email']
            titulo = formulario.cleaned_data['Titulo']
            texto = formulario.cleaned_data['Texto']

            to_admin = 'lusifertorresSS@gmail.com'
            html_content = "Informacion recibida de [%s] <br> <br> <br> **** Mensaje **** <br><br> %s"%(email,texto)
            msg = EmailMultiAlternatives('Correo de Contacto',html_content,'from@server.com', [to_admin])
            msg.attach_alternative(html_content,'text/html')
            msg.send()

        else:
            formulario = ClienteForm()
    formulario = ClienteForm()
    ctx = {'form':formulario,'email':email,'titulo':titulo,'texto':texto,'info_enviada':info_envianda}
    return render_to_response('cliente.html',ctx,context_instance=RequestContext(request))
