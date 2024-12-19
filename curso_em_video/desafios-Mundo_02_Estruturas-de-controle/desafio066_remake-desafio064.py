'''
Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuario digitar o valor 999, que e a condicao de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles. (Desconsiderando a flag)
'''
i = soma = 0
while True:
    n = int(input('Digite um numero inteiro [999 PARA PARAR]: '))
    if n == 999:
        break
    soma +=n
    i +=1

print(f'A soma dos {i} valores foi {soma}!')
