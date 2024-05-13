from django.shortcuts import render
from django.views import View
from .models import datosusuario
from django.shortcuts import redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def welcome(request):

    if request.user.is_authenticated:

        return render(request, "usuarios/bienvenido.html")
    
    return redirect('/login')

def login(request):
 
    form = AuthenticationForm()
    if request.method == "POST":
   
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
  
            user = authenticate(username=username, password=password)
 
            if user is not None:
             
                do_login(request, user)
          
                return redirect('/home')

        else:

            return render(request, "usuarios/logine.html", {'form': form}) 

    return render(request, "usuarios/login.html", {'form': form})

def logout(request):
 
    do_logout(request)
    return redirect('/')

class HomeView(View):
    def get(self, request, *args, **kwargs):
        
        context={

        }
        return render(request, 'pages/index.html', context)
    


def personal_perfil(request, id_persona):

    data = datosusuario.objects.get(id = id_persona)

    if request.method == 'POST':

        data.nombre = request.POST['nombre']
        data.area = request.POST['area']
        data.cargo = request.POST['cargo']
        data.email = request.POST['email']
        data.Telefono = request.POST['telefono']
        data.Comentarios = request.POST['comentarios']
        data.estado = request.POST['estado']
        try:
            data.fecha_nacimiento = request.POST['fecha_nacimiento']

        except:
            pass
        try:
            data.fecha_ingreso = request.POST['fecha_ingreso']
        except:
            pass
        data.save()

        return redirect('Perfil personal', id_persona = data.id)

    return render(request, 'usuarios/usuario_perfil.html', {'data':data})

