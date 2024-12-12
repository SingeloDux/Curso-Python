# Faca um programa que leia um numero inteiro e diga se ele e ou nao um numero primo. Sabendo que um numero primo so e divisivel SOMENTE por 1 e ele mesmo.

print('\n {:=^45}'.format('\033[1m VERIFICADOR DE NUMEROS PRIMOS \033[m'))

num = int(input('\nDigite um numero para saber se e ou nao primo: '))

total = 0
for i in range(1, num+1):
    if num % i == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')

    print('{}' .format(i), end='')

print('\n\033[mO numero {} foi divisivel {} vezes!' .format(num, total))

if total == 2:
    print('Por isso ele e PRIMO')
else:
    print('Por isso ele NAO E PRIMO')