# Faca um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

print('\n {:=^45}'.format('\033[1m ANALISE DE PESOS \033[m'))

maior = 0
menor = 0
for i in range (1,6):
    peso = float(input('Digite o peso da {}a pessoa: ' .format(i)))

    if i == 1:
        maior = peso
        menor = peso
    else: 
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('\nDos 7 pesos entrados, o MAIOR foi {}Kg e o MENOR foi {}Kg! ' .format(maior, menor))


