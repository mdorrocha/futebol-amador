from django.contrib import admin
from cadastros.models import Grupo, Local, ModalidadeFutebol, Posicao


@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    ordering = ['nome']
    list_display = ('data_criacao', 'nome', 'ativo')
    list_display_links = ('data_criacao', 'nome')
    

@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    ordering = ['nome']
    list_display = ('nome', 'endereco', 'cidade', 'ativo')
    list_display_links = ('nome', )


@admin.register(ModalidadeFutebol)
class ModalidadeFutebolAdmin(admin.ModelAdmin):
    ordering = ['nome']
    list_display = ('nome', 'quantidade_jogador')
    list_display_links = ('nome', )


@admin.register(Posicao)
class PosicaoAdmin(admin.ModelAdmin):
    ordering = ['nome']
    list_display = ('modalidade_futebol', 'nome')
    list_display_links = ('modalidade_futebol', )
