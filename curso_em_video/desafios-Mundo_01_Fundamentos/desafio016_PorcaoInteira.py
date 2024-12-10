# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porcao inteira. Ex: Ao digitar o numero 6.127, o programa exiba a parte inteira 6.

from math import floor, trunc

num = float(input('Digite um numero real qualquer: '))
print('O numero {} tem a parte inteira {} >>> Sem Modulo' .format(num, int(num)))
print('O numero {} tem a parte inteira {} >>> Floor' .format(num, floor(num)))
print('O numero {} tem a parte inteira {} >>> Truncate' .format(num, trunc(num)))
