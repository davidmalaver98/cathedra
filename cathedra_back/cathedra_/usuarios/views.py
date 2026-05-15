

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            error = 'Usuario o contraseña incorrectos'
    return render(request, 'login.html', {'error': error})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def inicio_view(request):
    return render(request, 'inicio.html')

def registro_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            error = 'Las contraseñas no coinciden'
        elif User.objects.filter(username=username).exists():
            error = 'El usuario ya existe'
        else:
            User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                password=password1
            )
            return redirect('login')
    return render(request, 'login.html', {'error': error})