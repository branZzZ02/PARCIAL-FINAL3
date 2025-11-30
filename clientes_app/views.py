from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Cliente
from .forms import ClienteForm

# --- 1. LOGIN (Entrada) ---
def entrar_sistema(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('panel_principal')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# --- 2. PANEL (Dashboard) ---
@login_required
def panel_principal(request):
    return render(request, 'dashboard.html')

# --- 3. SALIR ---
def cerrar_sesion_usuario(request):
    logout(request)
    return redirect('login')

# --- 4. TABLA (Listar) ---
@login_required
def lista_clientes(request):
    # Ordenado por el más reciente
    registros = Cliente.objects.all().order_by('-fecha_registro')
    return render(request, 'tabla.html', {'clientes': registros})

# --- 5. AGREGAR ---
@login_required
def nuevo_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Registrar Nuevo'})

# --- 6. EDITAR ---
@login_required
def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Actualizar Datos'})

# --- 7. ELIMINAR ---
@login_required
def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    return redirect('lista_clientes')