# Faca um programa que leia tres numeros e mostre qual e o maior e qual e o menor.

um = float(input('Digite o primeiro numero: '))
dois = float(input('Digite o segundo numero: '))
tres = float(input('Digite o terceiro numero: '))

if um > dois and um > tres:
    maior = um
elif dois > um and dois > tres:
    maior = dois
else:
    maior = tres

if um < dois and um < tres:
    menor = um
elif dois < um and dois < tres:
    menor = dois
else:
    menor = tres

print('{:.2f} e o maior dos tres numeros e {:.2f} e o menor deles.' .format(maior, menor))