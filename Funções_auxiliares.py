from math import floor
#Função para verificação da terceira carta
def verifica_compra(s_banco,mao_jogador):
    if s_banco >= 6:
        return False
    elif len(mao_jogador) == 2 and s_banco <= 5:
        return True
    else:
        if s_banco == 0 or s_banco == 1 or s_banco == 2:
            return True
        
        elif s_banco == 3 and mao_jogador[2] != 8:
            return True
        
        elif s_banco == 4 and mao_jogador[2] not in [0,1,8,9]:
            return True
        
        elif s_banco == 5 and mao_jogador[2] not in [0,1,2,3,8,9]:
            return True

        else:
            return False

def fichas_recebidas(fichas,valor_aposta,aposta,resultado,baralhos):
    if aposta == resultado:
        if resultado == 'jogador':
            if baralhos == 1:
                fichas += floor(valor_aposta * 0.9871)
            else: 
                fichas += floor(valor_aposta * 0.9876)


        elif resultado == 'banco':
            if baralhos == 1:
                fichas += floor((0.95 * valor_aposta) * 0.9899)
            else:
                fichas += floor((0.95 * valor_aposta) * 0.9894)

        else:
            if baralhos == 1:
                fichas += floor((8 * valor_aposta) * 0.8425)
            elif baralhos == 6:
                fichas += floor((8 * valor_aposta) * 0.8556)
            else:
                fichas += floor((8 * valor_aposta) * 0.8564)
    else:
        fichas -= valor_aposta
    
    return fichas



        

