# Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuario digitar o valor 999, que e a condicao de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles (Desconsiderando o flag)

print('\n {:=^45}'.format('\033[1;32m SOMANDO VARIOS NUMEROS! \033[m'))

num = soma = i = 0

while num != 999:
    num = int(input('Digite um numero inteiro (999 para sair): '))
    if num != 999:
        soma += num
        i +=1

print('\nVoce digitou {} numeros e a soma entre eles e {}! ' .format(i, soma))