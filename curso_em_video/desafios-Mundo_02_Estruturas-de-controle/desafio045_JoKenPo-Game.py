# Crie um programa que faça o computador jogar Jokenpô com você.
from asyncio import sleep
from random import randint

print('{:=^50}' .format('\033[1;34mGAME: Pedra Papel e Tesoura\033[m\n'))
print('FACA SUA ESCOLHA \n[1] - PEDRA \n[2] - PAPEL \n[3] - TESOURA')

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0,2)
jogador = int(input('Qual a sua jogada? : '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-='*30)
print('Computador jogou {}' .format(itens[computador]))
print('Voce jogou {}' .format(itens[jogador]))
print('-='*30)

if computador == 0: # PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCEU!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVALIDA!')
elif computador == 1: # PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU!')
    else:
        print('JOGADA INVALIDA!')
elif computador == 2: #TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVALIDA!')

