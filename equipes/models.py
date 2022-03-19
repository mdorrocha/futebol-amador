from django.db import models
from cadastros.models import Grupo, Posicao, ModalidadeFutebol, Local
from django.contrib.auth.models import User


class Jogador(models.Model):
    """"Nome dos jogadores"""
    class Meta:
        verbose_name_plural = 'Jogadores'

    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    data_nascimento = models.DateField(verbose_name='Data de nascimento', blank=True, null=True)
    posicao = models.ForeignKey(Posicao, verbose_name='Posição', on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True)
    pontuacao = models.PositiveSmallIntegerField(verbose_name='Pontuação', default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Equipe(models.Model):
    """"Nome das equipes pertencentes a um grupo de amigos"""
    data_criacao = models.DateTimeField(verbose_name='Data de criação', auto_now_add=True)
    nome = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/%d/%m/%Y', blank=True)

    def __str__(self):
        return self.nome


class Jogo(models.Model):
    """Informações sobre a partida de futebol"""
    data_hora_jogo = models.DateTimeField(verbose_name='Data e hora do jogo')
    modalidade_futebol = models.ForeignKey(ModalidadeFutebol, verbose_name='Modalidade de futebol', on_delete=models.CASCADE)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    presenca = models.ManyToManyField(Jogador, verbose_name='Presença')
    escalacao = models.ManyToManyField(Equipe, verbose_name='Escalação', through='EscalacaoJogo')
    gols_equipe_um = models.PositiveSmallIntegerField(verbose_name='Gols da equipe 1', default=0)
    gols_equipe_dois = models.PositiveSmallIntegerField(verbose_name='Gols da equipe 2', default=0)

    def __str__(self):
        return 'Jogo {0}'.format(self.id)


class EscalacaoJogo(models.Model):
    class Meta:
        verbose_name = 'Escalação do jogo'
        verbose_name_plural = 'Escalação dos jogos'
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    jogador = models.ForeignKey(Jogador, on_delete=models.CASCADE)

