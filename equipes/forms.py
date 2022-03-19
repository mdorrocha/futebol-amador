from django.forms import ModelForm
from equipes.models import Jogo


class JogoForm(ModelForm):
    class Meta:
        model = Jogo
        fields = ['data_hora_jogo', 'modalidade_futebol', 'local']
