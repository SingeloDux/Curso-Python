# Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja sao maiores! Considere 21 anos

from datetime import date
ano = date.today().year
maiores = 0
menores = 0


print('\n {:=^45}'.format('\033[1m VERIFICADOR DE IDADES \033[m'))

for i in range (0,7):
    anoNasc = int(input('Digite o {}o ano de nascimento: ' .format(i+1)))
    idade = ano - anoNasc
    if idade >= 21:
        maiores +=1
    else:
        menores +=1

print('\nDos 7 anos de nascimentos de entrada, {} sao maiores de idade, e {} ainda nao atingiram a maioridade! ' .format(maiores, menores))