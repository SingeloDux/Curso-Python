# Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo. Sabendo que: A soma de cada um dos segmentos deve ser menor que a soma do comprimento dos outros dois.

print('\033[1;34mVERIFICADOR DE RETAS PARA FORMAR TRIANGULO\033[m\n', '=-'*22)
r1 = float(input('Digite o comprimento da recta 1: '))
r2 = float(input('Digite o comprimento da recta 2: '))
r3 = float(input('Digite o comprimento da recta 3: '))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('Os segmentos informados PODEM FORMAR um triangulo!')
else:
    print('Os segmentos informados NAO PODEM FORMAR um triangulo!')