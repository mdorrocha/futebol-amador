from dataclasses import fields
from django.contrib import admin
from equipes.models import Equipe, EscalacaoJogo, Jogador, Jogo

@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    ordering = ['nome']
    list_display = ('data_criacao', 'nome')
    list_display_links = ('data_criacao', 'nome')


@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
    ordering = ['nome']
    list_display = ('nome', 'email', 'data_nascimento', 'posicao', 'pontuacao')
    list_display_links = ('nome', )


class PresencaInline(admin.TabularInline):
    model = Jogo.presenca.through


@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):
    ordering = ['data_hora_jogo']
    list_display = ('id', 'data_hora_jogo', 'modalidade_futebol', 'local')
    list_display_links = ('id', 'data_hora_jogo')
    fields = ['data_hora_jogo', 'modalidade_futebol', 'local', 'gols_equipe_um', 'gols_equipe_dois']
    inlines = [PresencaInline]
