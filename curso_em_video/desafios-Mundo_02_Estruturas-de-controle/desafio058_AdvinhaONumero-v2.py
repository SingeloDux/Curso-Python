# Melhore o jogo do desafio 028 onde o computador "pensa" em um numero entre 0 e 10. So que agora o jogador vai tentar advinhar ate acertar, mostrando no final quantos palpites foram necessarios para vencer

from random import randint
computador = randint(0,10)
print('\n {:=^45}'.format('\033[1;33m ADVINHE O NUMERO: O JOGO! \033[m'))

print('-='*30)
print('\033[31mPC disse: Acabei de pensar em um numero entre 0 e 10.\033[m')
print('-='*30)

jogador = int(input('Qual numero acabei de pensar? : '))
print('PROCESSANDO...')

palpites = 1
while jogador != computador:

    if computador > jogador:   
        jogador = int(input('\nPalpite Errado! Tente um numero MAIOR: '))
        palpites +=1
    else:
        jogador = int(input('\nPalpite Errado! Tente um numero MENOR: '))
        palpites +=1

print('\n\033[32mParabens! Depois de {} palpites, voce finalmente acertou!\033[m' .format(palpites))
