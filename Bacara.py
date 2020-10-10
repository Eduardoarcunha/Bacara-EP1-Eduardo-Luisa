# EP - Design de Software
# Equipe: Eduardo Araujo e Luisa Manzig
# Data: 18/10/2020

print('--------------------------- \n Bem Vindos ao jogo Bacará \n---------------------------')
#importando biblioteca random
from Funções_auxiliares import *
import random
jogo = True

#Valores de acordo com o bacara
cartas_valores = {'As':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':0,'K':0,'Q':0,'J':0}

#Cartas de um único baralho
cartas_baralho1 = 4 * ['As','2','3','4','5','6','7','8','9','10','K','Q','J'] #52 cartas

#Mão do jogador + banco
maos = [ [] for _ in range(0,2) ]


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
nj = int(input('Número de pessoas: '))
while True:
    if nj <= 0:
        print('Número inválido...')
        nj = int(input('Número de pessoas: '))
    else:
        break

#lista dos vencedores
vencedores = []


opcoes = ['jogador','banco','empate']


fichas = [100] * nj

#verificando apostas
while jogo:
    soma = [0] * 2
    apostas = []
    valor_aposta = []
    for a in range(0, nj):
        if fichas[a] > 0:
            print('Jogador {}, qual sua aposta? (empate, banco ou jogador)'.format(a + 1))
            b = input()
            while True:
                if b in opcoes:
                    apostas.append(b)
                    break
                else:
                    print('Aposta invalida...')
                    print('Jogador {}, qual sua aposta? (empate, banco, ou jogador)'.format(a + 1))
                    b = input()

            print('Jogador {}, de quanto é sua aposta?'.format(a + 1))
            b = int(input())
            while True:
                if b > 0 and b <= fichas[a]:
                    valor_aposta.append(b)
                    break
                else:
                    print('Aposta invalida...')
                    print('Jogador {}, de quanto é sua aposta? '.format(a + 1))
                    b = int(input())
        if fichas[a] <= 0:
            apostas.append('eliminado')
            valor_aposta.append('eliminado')

    print('chegou')

    i = 0

    #distribuição das duas primeiras cartas
    while i < 2:
        for s in range(0,2):
                x = random.randint(0,len(cartas_baralho)-1)
                maos[s].append(cartas_baralho[x])
                del cartas_baralho[x]
        i += 1

    #soma das duas primeiras cartas
    for s in range(0,2):
        for t in range(0,2):
            soma[s] += cartas_valores[maos[s][t]]
            if soma [s] >= 10:
                soma[s] -= 10

    
    ciclo = True
    #Ciclo até existir um vencedor ou empate
    while ciclo:
        for i,s in enumerate(soma):
            if s == 8 or s == 9:
                if i == 0:
                    vencedores.append('jogador')
                elif i == 1:
                    vencedores.append('banco')

        if len(vencedores) == 1 or len(vencedores) == 2:
            break
        else:
            if soma[0] <= 5:
                x = random.randint(0,len(cartas_baralho) - 1)
                maos[0].append(cartas_baralho[x])
                del(cartas_baralho[x])
                soma[0] += cartas_valores[maos[0][2]]
                if soma[0] >= 10:
                    soma[0] -= 10
            
            if verifica_compra(soma[1],maos[0]):
                x = random.randint(0,len(cartas_baralho) - 1)
                maos[1].append(cartas_baralho[x])
                del(cartas_baralho[x])
                soma[1] += cartas_valores[maos[1][2]]
                if soma[1] >= 10:
                    soma[1] -= 10            

        for i,s in enumerate(soma):
            if s == 8 or s == 9:
                if i == 0:
                    vencedores.append('jogador')
                elif i == 1:
                    vencedores.append('banco')


    print('chegou')

    #Conferindo resultados
    if len(vencedores) == 0 or len(vencedores) == 2:
        resultado = 'empate'
    else:
        if vencedores[0] == 'jogador':
            resultado = 'jogador'
        else:
            resultado = 'banco'

    for i in range(0,nj - 1):
        if fichas[i] > 0:
            fichas[i] = fichas_recebidas(fichas[i],valor_aposta[i],apostas[i],resultado,nb)

    while True:
        d = input('Quer continuar jogando(sim/não)')
        if d == 'não':
            jogo = False
            break
        elif d == 'sim':
            break
        else:
            print('Resposta invalida')
        


    print(apostas,valor_aposta,maos,soma,vencedores,resultado)