# Faca um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la. Sabendo que cada litro de tinta, pinta uma area de 2m2.

print('='*5, 'Calculadora de tinta necessaria para pintar uma parede!', '='*5)

largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura*altura
tinta = area/2

print('Para pintar uma parede com a area de {:.2f}m2, vai ser preciso uma quantidade de {:.2f}litros de tinta!' .format(area, tinta))

