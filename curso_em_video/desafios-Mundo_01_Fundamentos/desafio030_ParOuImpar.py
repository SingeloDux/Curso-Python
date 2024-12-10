# Crie um programa que leia um numero inteiro qualquer e mostre na tela se ele e PAR ou IMPAR.

num = int(input('Digite um numero qualquer para saber se ele e PAR ou IMPAR: '))

if num % 2 == 0:
    print('O numero \033[33m{}\033[m e PAR' .format(num))
else:
    print('O numero \033[33m{}\033[m e IMPAR' .format(num))