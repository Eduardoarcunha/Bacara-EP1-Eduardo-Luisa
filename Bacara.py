# EP - Design de Software
# Equipe: Eduardo Araujo e Luisa Manzig
# Data: 18/10/2020

print('--------------------------- \n Bem Vindos ao jogo Bacará \n---------------------------')
#Importando bibliotecas e "ligando" o jogo
from Funções_auxiliares import *
import random
jogo = True


#Valores das cartas de acordo com o bacara
cartas_valores = {'As':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':0,'K':0,'Q':0,'J':0}

#Cartas de um único baralho
cartas_baralho1 = 4 * ['As','2','3','4','5','6','7','8','9','10','K','Q','J'] #52 cartas

#Perguntando sobre as regras
c = input('Gostaria de saber as regras? (sim/nao)')
if c == 'sim':
    print(regras)

#Quantos baralhos (nb) serão utilizados
nb = int(input('Quantos baralhos serão utilizados? (1,6,8): '))
while True:
    if nb == 1 or nb == 6 or nb == 8:
        break
    else: 
        print('Número inválido...')
        nb = int(input('Quantos baralhos serão utilizados? (1,6,8): '))

cartas_baralho = nb * cartas_baralho1

#Quantos jogadores (nj) vão jogar
nj = int(input('Número de pessoas: '))
while True:
    if nj <= 0:
        print('Número inválido...')
        nj = int(input('Número de pessoas: '))
    else:
        break

#Opções de aposta e fichas iniciais
opcoes = ['jogador','banco','empate']
fichas = [100] * nj

#Verificando apostas e os valores
while jogo:
    cartas_baralho = nb * cartas_baralho1
    vencedores = []
    maos = [ [] for _ in range(0,2) ]
    soma = [0] * 2
    apostas = []
    valor_aposta = []
    for a in range(0, nj):
        if fichas[a] > 0:
            print('Jogador {}, qual sua aposta? (jogador, banco ou empate)'.format(a + 1))
            c = input()
            while True:
                if c in opcoes:
                    apostas.append(c)
                    break
                else:
                    print('Aposta inválida... Digite um resultado.')
                    print('Jogador {}, qual sua aposta? (jogador, banco ou empate)'.format(a + 1))
                    c = input()

            print('Jogador {}, de quanto é sua aposta?'.format(a + 1))
            while True:
                try: 
                    c = int(input())
                    if c > 0 and c <= fichas[a]:
                        valor_aposta.append(c)
                        break
                    else:
                        print('Aposta inválida... Certifique-se da sua quantia.')
                        print('Jogador {}, de quanto é sua aposta? '.format(a + 1))
                        c = int(input())
                except ValueError: 
                    print('Aposta inválida... Digite um valor numérico.')
                    print('Jogador {}, de quanto é sua aposta? '.format(a + 1))
        if fichas[a] <= 0:
            apostas.append('Eliminado')
            valor_aposta.append('Eliminado')

    for a in range(0, nj):
        if fichas[a] > 0:
            print('Jogador {0} sua aposta foi de {1} fichas no {2}.'.format((a+1), valor_aposta[a], apostas[a]))

    #Distribuição das duas primeiras cartas
    i = 0
    while i < 2:
        for a in range(0,2):
                x = random.randint(0,len(cartas_baralho)-1)
                maos[a].append(cartas_baralho[x])
                del cartas_baralho[x]
        i += 1

    #soma das duas primeiras cartas
    for a in range(0,2):
        for t in range(0,2):
            soma[a] += cartas_valores[maos[a][t]]
            if soma [a] >= 10:
                soma[a] -= 10

    #Ciclo até existir um vencedor ou empate
    ciclo = True
    while ciclo:
        for i, a in enumerate(soma):
            if a == 8 or a == 9:
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

        for i, a in enumerate(soma):
            if a == 8 or a == 9:
                if i == 0:
                    vencedores.append('jogador')
                elif i == 1:
                    vencedores.append('banco')
        break
    print('\nMão dos jogadores: {0} \nSoma:{1}'.format(maos[0], soma[0]))
    print('Mão do banco: {0} \nSoma:{1}\n'.format(maos[1], soma[1]))
    
    #Conferindo os resultados e jogadores eliminados
    if len(vencedores) == 0 or len(vencedores) == 2:
        resultado = 'empate'
    else:
        if vencedores[0] == 'jogador':
            resultado = 'jogador'
        else:
            resultado = 'banco'

    if resultado == 'empate':
        print('O resultado foi {0}.'.format(resultado))
    else:
        print('O {0} venceu!'.format(resultado))

    for a in range(0, nj):
        if fichas[a] > 0:
            fichas[a] = fichas_recebidas(fichas[a],valor_aposta[a],apostas[a],resultado,nb)
            if fichas[a] == 0:
                print('Jogador {}, você foi eliminado...'.format(a + 1))

    for i, a in enumerate(fichas):
        print('O saldo de fichas do jogador {0} ficou: {1}.'.format(i+1, a))

    while True:
        saldo = True
        for a in range(0,nj):
            if fichas[a] != 0 and a < nj - 1:
                saldo = True
                break
            elif a == nj - 1 and fichas[a] == 0:
                saldo = False

        if not saldo:
            print('\nTodos jogadores foram eliminados...\n')
            jogo = False
            break
        while saldo:
            c = input('Quer continuar jogando? (sim/nao):')
            if c == 'nao':
                jogo = False
                print('Jogo finalizado. \n \n')
                break
            elif c == 'sim':
                break
            else:
                print('Resposta inválida...')
        break

for i, a in enumerate(fichas):
        print('O saldo de fichas final do jogador {0} é: {1}.'.format(i+1, a))

print('\nObrigado por jogar o Bacará!')