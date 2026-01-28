from django.shortcuts import render


def home(request):
    return render(request, 'users/home.html')


def login_view(request):
    return render(request, 'users/login.html')

def registar(request):
    return render(request, 'users/registar.html')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def registar(request):
    if request.method == 'POST':
        # 1. Recolher os dados do formulário (os 'name' dos inputs HTML)
        email = request.POST.get('email')
        instituicao = request.POST.get('instituicao')
        idade = request.POST.get('idade')
        ano_letivo = request.POST.get('ano_letivo')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # 2. Validação: As passwords são iguais?
        if password != confirm_password:
            messages.error(request, "As palavras-passe não coincidem!")
            return render(request, 'users/registar.html')

        # 3. Validação: O username já existe?
        if User.objects.filter(username=username).exists():
            messages.error(request, "Este nome de utilizador já está em uso.")
            return render(request, 'users/registar.html')

        # 4. Criar o Utilizador
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        
        # NOTA: Por agora, os dados de idade/escola não são guardados 
        # porque precisamos de criar um "Profile" na base de dados (ver próximo passo).
        
        messages.success(request, "Conta criada com sucesso! Podes agora entrar.")
        return redirect('login')

    return render(request, 'users/registar.html')