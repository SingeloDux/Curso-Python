# Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor e maior, O segundo valor e maior, Nao existe valor maior, os dois sao iguais.

print('COMPARADOR DE NUMEROS\n', '=-'*25)

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1>n2:
    print('O PRIMEIRO numero e maior!')
elif n2>n2:
    print('O SEGUNDO numero e maior!')
else:
    print('Os dois SAO IGUAIS!')
