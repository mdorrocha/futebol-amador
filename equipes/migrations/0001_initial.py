# Generated by Django 3.2.5 on 2022-02-01 01:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('nome', models.CharField(max_length=100)),
                ('logo', models.ImageField(blank=True, upload_to='logos/%d/%m/%Y')),
            ],
        ),
        migrations.CreateModel(
            name='EscalacaoJogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipes.equipe')),
            ],
            options={
                'verbose_name': 'Escalação do jogo',
                'verbose_name_plural': 'Escalação dos jogos',
            },
        ),
        migrations.CreateModel(
            name='Jogador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de nascimento')),
                ('foto', models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y')),
                ('ranking', models.PositiveSmallIntegerField(default=0, verbose_name='Ranking')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.grupo')),
                ('posicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.posicao', verbose_name='Posição')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Jogadores',
            },
        ),
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora_jogo', models.DateTimeField(verbose_name='Data e hora do jogo')),
                ('gols_equipe_um', models.PositiveSmallIntegerField(default=0, verbose_name='Gols da equipe 1')),
                ('gols_equipe_dois', models.PositiveSmallIntegerField(default=0, verbose_name='Gols da equipe 2')),
                ('escalacao', models.ManyToManyField(through='equipes.EscalacaoJogo', to='equipes.Equipe', verbose_name='Escalação')),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.local')),
                ('modalidade_futebol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.modalidadefutebol', verbose_name='Modalidade de futebol')),
                ('presenca', models.ManyToManyField(to='equipes.Jogador', verbose_name='Presença')),
            ],
        ),
        migrations.AddField(
            model_name='escalacaojogo',
            name='jogador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipes.jogador'),
        ),
        migrations.AddField(
            model_name='escalacaojogo',
            name='jogo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipes.jogo'),
        ),
    ]