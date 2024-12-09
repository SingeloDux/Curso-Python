# Faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot
oposto = float(input('Informe a medida do cateto oposto: '))
adjacente = float(input('Informe a medida do cateto adjacente: '))

mathWay = (oposto ** 2 + adjacente ** 2) ** (1/2)
print('O comprimento da hipotenusa e {:.2f} | Sem Modulo'.format(mathWay))

hipotenusa = hypot(oposto, adjacente)
print('O comprimento da hipotenusa e {:.2f} | Com Modulo'.format(hipotenusa))
