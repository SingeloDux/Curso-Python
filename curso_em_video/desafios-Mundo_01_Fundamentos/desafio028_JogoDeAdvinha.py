# Escreva um programa que faca o computador "pensar" em um jogadorero inteiro entre 0 e 5 e peca para o usuario tentar descobrir qual foi o jogadorero computador pelo computador. O programa devera escrever na tela se o usuario venceu ou perdeu!
from random import randint
computador = randint(0,5)
print('-='*30)
print('Acabo de pensar em um jogadorero entre 0 e 5. Tente advinhar...')
print('-='*30)

jogador = int(input('Qual jogadorero acabei de pensar? : '))
print('PROCESSANDO...')

if computador == jogador:
    print('\nPARABENS, VOCE VENCEU! Realmente pensei no jogadorero {}!' .format(computador, jogador))
else:
    print('\nVOCE PERDEU! Eu pensei no jogadorero {} e nao {}!' .format(computador, jogador))
