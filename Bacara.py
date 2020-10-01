# EP - Design de Software
# Equipe: Eduardo Araujo e Luisa Manzig
# Data: 18/10/2020

print('--------------------------- \n Bem Vindos ao jogo Bacará \n---------------------------')
#importando biblioteca random
import random

#Valores de acordo com o bacara
cartas_valores = {'As':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':0,'K':0,'Q':0,'J':0}

#Cartas de um único baralho
cartas_baralho1 = 4 * ['As','2','3','4','5','6','7','8','9','10','K','Q','J'] #52 cartas

#mãos do jogador e banco
banco = []

#Quantos baralhos
nb = int(input('Quantos baralhos serão utilizados? (1,6,8): '))
while True:
    if nb == 1 or nb == 6 or nb == 8:
        break
    else: 
        print('Número inválido...')
        nb = int(input('Quantos baralhos serão utilizados? (1,6,8): '))

cartas_baralho = nb * cartas_baralho1


#quantos jogadores vão jogar
j = int(input('Número de pessoas: '))
while True:
    if j <= 0:
        print('Número inválido...')
        j = int(input('Número de pessoas: '))
    else:
        break


indices_jogadores = []
for c in range(1, j+2):
    if c < (j+1):
        indices_jogadores.append(str(c))
    else:
        indices_jogadores.append('banco')
        indices_jogadores.append('empate')
print(indices_jogadores)

#verificando apostas
apostas = []
valor_aposta = []
for a in range(0, j):
    print('Jogador {}, qual sua aposta? (empate, banco, ou número jogador)'.format(a + 1))
    b = input()
    while True:
        if b in indices_jogadores:
            apostas.append(b)
            break
        else:
            print('Aposta invalida...')
            print('Jogador {}, qual sua aposta? (empate, banco, ou número jogador)'.format(a + 1))
            b = input()
    print('Jogador {}, de quanto é sua aposta?'.format(a + 1))
    b = int(input())
    while True:
        if b > 0 and b <= 100:
            valor_aposta.append(b)
            break
        else:
            print('Aposta invalida...')
            print('Jogador {}, de quanto é sua aposta? '.format(a + 1))
            b = int(input())
print(apostas)
print(valor_aposta)


#mão de jogadores + banco
maos_dos_jogadores = [ [] for _ in range(j + 1) ]


i = 0

while i < 2:
    for s in range(0,j+1):
        x = random.randint(0,len(cartas_baralho)-1)
        maos_dos_jogadores[s].append(cartas_baralho[x])
        del cartas_baralho[x]
    i += 1


soma = [0] * (j+1)
