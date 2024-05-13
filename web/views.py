from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import formularioWeb
# Create your views here.

def appWeb(request):
    return render(request, "web/web.html")
    
    

def separar_lote(request):
    if request.method=='POST':
        form = formularioWeb(request.POST)
        if form.is_valid():
            form.save()
            return redirect("web:pag_web") # redd a una pag que diga que ya se separo xd
    else:
        form = formularioWeb()
         
    return render(request, "web/separar_lote.html", {'form': form})



def listar(request):
    web = Web.objects.all()
    return render(request, 'web/listar_compras.html', {'web':web})

def pag_web(request):
    return render(request, 'web/pag_web.html')