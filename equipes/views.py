from django.shortcuts import render, redirect
from equipes.utils import gera_escalacao
from equipes.models import Jogo, Jogador, EscalacaoJogo, Equipe
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone


def index(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def lista_confirmados(request):
    jogo = Jogo.objects.last()
    confirmados = jogo.presenca.all()
    jogador = Jogador.objects.get(user=request.user)
    context = {'jogo': jogo, 'confirmados': confirmados}
    if request.method == "GET":        
        if not jogador in confirmados and not jogo.escalacao.all() and timezone.now() < jogo.data_hora_jogo:
            context.update({'confirmar_presenca': True})
    else:
        if bool(request.POST.get('confirmaPresenca')): 
            jogo.presenca.add(jogador)       
            messages.add_message(request, messages.SUCCESS, f'Presença confirmada {jogador.nome}. Agora é só mostrar tua habilidade!')
    return render(request, 'lista_confirmados.html', context)

@login_required(login_url='login')
def remover_presenca(request, id):
    if request.method == 'GET':
        jogo = Jogo.objects.last()
        jogador = Jogador.objects.get(id=id)
        if jogador.user == request.user:
            jogo.presenca.remove(jogador)
            messages.add_message(request, messages.SUCCESS, f'Que pena {jogador.nome}, a tua participação no jogo foi cancelada. Até a próxima!')
    return redirect('lista-confirmados')

@login_required(login_url='login')
def resultado(request):
    if request.method == 'GET':
        jogo = Jogo.objects.last()
    return render(request, 'resultado.html', {'jogo': jogo})

@login_required(login_url='login')
def ranking(request):
    grupo = Jogador.objects.get(user=request.user).grupo
    lista_atletas = Jogador.objects.filter(grupo=grupo).order_by('pontuacao', 'nome')
    return render(request, 'ranking.html', {'lista_atletas': lista_atletas})

@login_required(login_url='login')
def escalacao(request):
    jogo = Jogo.objects.last()
    equipes = Equipe.objects.all()
    context = {'jogo': jogo}
    if request.method == 'GET':
        total_confirmados = jogo.presenca.count()//2
        if equipes.count() > 1 and total_confirmados >= jogo.modalidade_futebol.quantidade_jogador:
            context.update({'tem_equipe_atletas': True}) 
    else:
        gera_escalacao(jogo)
    if jogo.escalacao.all():  
        equipe_um = EscalacaoJogo.objects.filter(equipe=equipes[0], jogo=jogo).order_by('jogador__posicao__nome')  
        equipe_dois = EscalacaoJogo.objects.filter(equipe=equipes[1], jogo=jogo).order_by('jogador__posicao__nome')
        context.update({'tem_escalacao': True, 'equipe_um': equipe_um, 'equipe_dois': equipe_dois})
    return render(request, 'escalacao.html', context)

def get_login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('index')
    else:
        nome = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = authenticate(request, username=nome, password=senha)
        if user:
            login(request, user)
            return redirect('index')
        messages.add_message(request, messages.ERROR, 'Suas credenciais estão incorretas')
    return render(request, 'login.html')

def get_logout(request):
    logout(request)
    return redirect('index')
        

