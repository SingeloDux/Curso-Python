# Faca um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo

from math import cos, sin, tan, radians
valor = float(input('Informe um angulo para saber o sen, cos e tg: '))

angulo = radians(valor) #Converter o angulo para radianos

print('Para o angulo de {} temos o: \nSENO: {:.2f} \nCOSSENO: {:.2f} \nTANGENTE: {:.2f}' .format(angulo, sin(angulo), cos(angulo), tan(angulo)))