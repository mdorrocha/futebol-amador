# Generated by Django 3.2.5 on 2022-02-01 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do grupo')),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ModalidadeFutebol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('quantidade_jogador', models.PositiveSmallIntegerField(verbose_name='Quantidade de jogadores')),
            ],
            options={
                'verbose_name': 'Modalidade de Futebol',
                'verbose_name_plural': 'Modalidades de Futebol',
            },
        ),
        migrations.CreateModel(
            name='Posicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('modalidade_futebol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.modalidadefutebol')),
            ],
            options={
                'verbose_name': 'Posição',
                'verbose_name_plural': 'Posições',
            },
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100, verbose_name='Endereço')),
                ('cidade', models.CharField(blank=True, max_length=50, null=True)),
                ('ativo', models.BooleanField(default=True)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.grupo')),
            ],
            options={
                'verbose_name_plural': 'Locais',
            },
        ),
    ]