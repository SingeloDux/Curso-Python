# Desenvolva um programa que leiao o primeiro termo e a razao de uma PA. No final, mostre os 10 primeiros termos dessa progressao.

print('\n {:=^45}'.format('\033[1m 10 TERMOS DUMA PROGRESSAO ARITMETICA \033[m'))

termo1 = int(input('\nDigite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
decimo = termo1 + (10-1) * razao

print('\nOs 10 primeiros termos da PA sao: ', end='')

for i in range (termo1, decimo + razao, razao):
    print('{}' .format(i), end='>>> ')
print('\nFIM')