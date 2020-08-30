from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from .forms import *
# Create your views here.

def inicio (request):
    return HttpResponse("HOLA")


def VerHoja(request):
    hojas=Hoja.objects.all()
    contexto = {'hojas':hojas}
    return render(request,'verhoja.html',contexto)



def CrearHoja(request):
    form=FormHoja()
    if request.method=='POST':
        form=FormHoja(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/verhoja')

    contexto = {'form':form}
    return render(request,'crearhoja.html',contexto)


def EditarHoja(request,id):
    hoja=Hoja.objects.get(idhoja=id)
    form=FormHoja(request.POST or None,instance=hoja)
    if form.is_valid():
        form.save()
        return redirect('/verhoja')

    contexto = {'form':form,'hoja':hoja}
    return render(request,'editarhoja.html',contexto)

def EliminarHoja(request,id):
    hoja=Hoja.objects.get(idhoja=id)
    if request.method=='POST':
        hoja.delete()
        return redirect('/verhoja')
    return render(request,'eliminarhoja.html',{'hoja':hoja})

def Ver(request,id):
    hoja=Hoja.objects.get(idhoja=id)
    contexto = {'hoja':hoja}
    return render(request,'ver.html',contexto)
