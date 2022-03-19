from django.urls import path
from equipes import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista-confirmados', views.lista_confirmados, name='lista-confirmados'),
    path('remover-presenca/<int:id>', views.remover_presenca, name='remover-presenca'),
    path('escalacao', views.escalacao, name='escalacao'),
    path('resultado', views.resultado, name='resultado'),
    path('ranking', views.ranking, name='ranking'),
    path('login', views.get_login, name='login'),
    path('logout', views.get_logout, name='logout'),
]