from collections import Counter
import random
from equipes.models import Equipe, EscalacaoJogo

def gera_escalacao(jogo):
    lista_confirmados = list(jogo.presenca.all())
    # embaralha os valores
    random.shuffle(lista_confirmados)
    c1 = Counter()
    c2 = Counter()
    equipes = Equipe.objects.all()
    EscalacaoJogo.objects.filter(jogo=jogo).delete()
    for jogador in lista_confirmados:
        nome = jogador.posicao.nome
        escalacao_equipe_um = EscalacaoJogo.objects.filter(equipe=equipes[0], jogo=jogo)
        escalacao_equipe_dois = EscalacaoJogo.objects.filter(equipe=equipes[1], jogo=jogo)
        if c2[nome] < c1[nome] or escalacao_equipe_dois.count() < escalacao_equipe_um.count():
            c2.update([nome])
            EscalacaoJogo.objects.create(equipe=equipes[1], jogo=jogo, jogador=jogador)
        else:            
            c1.update([nome])
            EscalacaoJogo.objects.create(equipe=equipes[0], jogo=jogo, jogador=jogador)    
                    