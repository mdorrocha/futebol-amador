from django.db import models

class Grupo(models.Model):
    """Nome do grupo de amigos que se diverte jogando futebol e claro, tomando umas cervejinhas depois."""

    data_criacao = models.DateTimeField(verbose_name='Data de criação', auto_now_add=True)
    nome = models.CharField(verbose_name='Nome do grupo', max_length=100)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class ModalidadeFutebol(models.Model):
    class Meta:
        verbose_name = 'Modalidade de Futebol'
        verbose_name_plural = 'Modalidades de Futebol'
    nome = models.CharField(max_length=50)
    quantidade_jogador = models.PositiveSmallIntegerField(verbose_name='Quantidade de jogadores')

    def __str__(self):
        return self.nome


class Posicao(models.Model):    
    class Meta:
        verbose_name = 'Posição'
        verbose_name_plural = 'Posições'
    modalidade_futebol = models.ForeignKey(ModalidadeFutebol, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Local(models.Model):
    class Meta:
        verbose_name_plural = 'Locais'

    nome = models.CharField(max_length=100)
    endereco = models.CharField(verbose_name='Endereço', max_length=100)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    ativo = models.BooleanField(default=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


