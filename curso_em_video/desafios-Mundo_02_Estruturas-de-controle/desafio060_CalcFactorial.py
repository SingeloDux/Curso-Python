# Faca um programa que leia um numero qualquer e mostre o seu fatorial. Ex: 5! = 5x4x3x2x1=120
from math import factorial

print('\n {:=^45}'.format('\033[1;33m CALCULADORA DE FATORIAIS \033[m'))

n = int(input('Digite um numero para calcular seu fatorial: '))
print('O fatorial de {}! = ' .format(n), end='')

#f = factorial(n)
#print('\nO fatorial de {}! e {}' .format(n, f))

i = n
f = 1
while i > 0:
    print('{}' .format(i), end='')
    print(' x ' if  i > 1 else ' = ', end='')
    f *= i
    i-=1

print('{}' .format(f))

print('\nFIM')