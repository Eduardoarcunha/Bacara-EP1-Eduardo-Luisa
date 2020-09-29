# EP - Design de Software
# Equipe: Eduardo Araujo e Luisa Manzig
# Data: 18/10/2020


#importando biblioteca random
import random

#Valores de acordo com o bacara
cartas_valores = {'As':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':0,'K':0,'Q':0,'J':0}

#Cartas de um único baralho
cartas_baralho = 4 * ['As','2','3','4','5','6','7','8','9','10','K','Q','J'] #52 cartas

#mãos do jogador e banco
banco = []

#quantos jogadores vão jogar
j = int(input('Número de pessoas'))

#mão de jogadores + banco
maos_dos_jogadores = [ [] for _ in range(j + 1) ]


i = 0

while i < 2:
    for s in range(0,j+1):
        x = random.randint(0,51)
        maos_dos_jogadores[s].append(cartas_baralho[x])
        del cartas_baralho[x]
    i += 1


