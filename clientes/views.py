from django.shortcuts import render, redirect
from .models import Cliente
from django.shortcuts import get_object_or_404
from .forms import *
from django.views.generic import ListView, CreateView


def app_clientes(request):
    return render(request, 'clientes/app_clientes.html')

def clientes(request):
    lista_clientes = Cliente.objects.all()
    data = {
        'lista_clientes' :lista_clientes,
    }
    return render(request, 'clientes/clientes.html', data)


def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes:clientes')
        
    else:
        form = ClienteForm()
    return render(request, 'clientes/crear_cliente.html', {'form': form})

def ver_cliente(request, pk):
    cliente = get_object_or_404(Cliente, id=pk)
    return render(request, 'clientes/ver_cliente', {'cliente': cliente})



def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, id=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes:clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/editar_cliente.html', {'form': form})




def eliminar_cliente(request, pk):  
    cliente = get_object_or_404(Cliente, id=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes:listar_proyectos')
    return render(request, 'clientes/eliminar_cliente.html', {'cliente': cliente})





# SEPARAR LOTES



def listar_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'clientes/lotes/lista_ventas.html', {'ventas': ventas})

def crear_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            try:
                venta = form.save(commit=False)
                venta.cuotas = form.cleaned_data['cuotas']  # Obtener las cuotas del formulario
                venta.save()

                subproyecto = venta.subproyecto
                subproyecto.estado = 'SEPARADO'
                subproyecto.save()
                return redirect('clientes:listar_ventas')
            except ValueError as e:
                error_message = str(e)
                return render(request, 'clientes/lotes/crear_venta.html', {'form': form, 'error_message': error_message})
    else:
        proyecto_id = request.GET.get('proyecto')
        form = VentaForm(proyecto_id=proyecto_id)  # Pasa el ID del proyecto al formulario

    return render(request, 'clientes/lotes/crear_venta.html', {'form': form})



def ver_venta(request, venta_id):
    venta = get_object_or_404(Venta, pk=venta_id)
    return render(request, 'clientes/lotes/ver_venta.html', {'venta': venta})

def actualizar_venta(request, venta_id):
    venta = get_object_or_404(Venta, pk=venta_id)
    if request.method == 'POST':
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('listar_ventas')
    else:
        form = VentaForm(instance=venta)
    return render(request, 'clientes/lotes/actualizar_venta.html', {'form': form})

def eliminar_venta(request, venta_id):
    venta = get_object_or_404(Venta, pk=venta_id)
    if request.method == 'POST':
        venta.delete()
        return redirect('listar_ventas')
    return render(request, 'clientes/lotes/confirmar_eliminar_venta.html', {'venta': venta})


# cuotas

def listar_cuotas(request):
    cuotas = Cuota.objects.all()
    return render(request, 'clientes/cuotas/lista_cuotas.html', {'cuotas': cuotas})

def crear_cuota(request):
    if request.method == 'POST':
        form = CuotaForm(request.POST)
        if form.is_valid():
            cuota = form.save()
            return redirect('clientes:detalle_cuota', pk=cuota.venta.pk)  
    else:
        form = CuotaForm()
    return render(request, 'clientes/cuotas/crear_cuota.html', {'form': form})


def detalle_cuota(request, pk):
    venta = Venta.objects.get(pk=pk)
    cuotas = Cuota.objects.filter(venta=venta)
    return render(request, 'clientes/cuotas/detalle_cuota.html', {'venta': venta, 'cuotas': cuotas})
