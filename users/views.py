from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Perfil  # IMPORTANTE: Adicionado para o Django reconhecer a tabela Perfil

def home(request):
    return render(request, 'users/home.html')

def login_view(request):
    return render(request, 'users/login.html')

def registar(request):
    if request.method == 'POST':
        # 1. Recolher os dados do formulário
        email = request.POST.get('email')
        instituicao = request.POST.get('instituicao')
        idade = request.POST.get('idade')
        ano_letivo = request.POST.get('ano_letivo')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # 2. Validações
        if password != confirm_password:
            messages.error(request, "As palavras-passe não coincidem!")
            return render(request, 'users/registar.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Este nome de utilizador já está em uso.")
            return render(request, 'users/registar.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        
        Perfil.objects.create(
            user=user, 
            instituicao=instituicao, 
            idade=idade, 
            ano_letivo=ano_letivo
        )
        
        messages.success(request, "Conta criada com sucesso! Podes agora entrar.")
        return redirect('login')

    # Se for um pedido GET (abrir a página), mostra o formulário
    return render(request, 'users/registar.html')

def sobrenos(request):
    return render(request, 'users/sobrenos.html')

def home2(request):
    return render(request, 'users/home2.html')

def quiz(request):
    perguntas = [
        {"id": 1, "p": "Qual destas senhas é a mais segura?", "o": ["123456", "admin", "P@ssw0rd2024!", "marcelo123"], "c": "P@ssw0rd2024!"},
        {"id": 2, "p": "O que é o Phishing?", "o": ["Um desporto", "Um ataque por email", "Um antivírus", "Um tipo de ecrã"], "c": "Um ataque por email"},
        {"id": 3, "p": "Deves partilhar a tua localização nas redes sociais?", "o": ["Sim, sempre", "Só com estranhos", "Não, por segurança", "Apenas à noite"], "c": "Não, por segurança"},
        {"id": 4, "p": "O que significa o cadeado no navegador?", "o": ["Site lento", "Site perigoso", "Conexão segura", "Site bloqueado"], "c": "Conexão segura"},
        {"id": 5, "p": "De quanto em quanto tempo deves mudar a senha?", "o": ["Nunca", "Anualmente", "Regularmente", "Todos os dias"], "c": "Regularmente"},
        {"id": 6, "p": "A autenticação de dois fatores (2FA) serve para:", "o": ["Mais velocidade", "Dupla segurança", "Gastar bateria", "Ver vídeos"], "c": "Dupla segurança"},
        {"id": 7, "p": "Se receberes um link estranho de um amigo, deves:", "o": ["Clicar logo", "Ignorar e avisá-lo", "Enviar a outros", "Apagar o PC"], "c": "Ignorar e avisá-lo"},
    ]
    passo = request.session.get('quiz_step', 0)

    if request.method == 'POST':
        passo += 1
        request.session['quiz_step'] = passo
        
        if passo >= 7:
            request.session['quiz_step'] = 0 # Reset para a próxima vez
            return render(request, 'users/quiz_final.html') # Página de parabéns

    pergunta_atual = perguntas[passo]
    context = {
        'pergunta': pergunta_atual,
        'numero': passo + 1,
        'progresso': (passo + 1) * 100 / 7
    }
    return render(request, 'users/quiz.html', context)

