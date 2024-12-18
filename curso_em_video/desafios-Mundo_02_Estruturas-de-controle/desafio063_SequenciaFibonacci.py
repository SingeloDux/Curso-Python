# Escreva um programa que leia um numero n inteiro e mostre na tela os n primeiros elementos de uma sequencia de Fibonacci. Ex: 0 > 1 > 1 > 2 > 5 > 8

print('\n {:=^45}'.format('\033[1;32m SEQUENCIA FIBONNACI! \033[m'))

n = int(input('Quantos termos da sequencia quer exibir? : '))

t1 = 0
t2 = 1
i = 3
print('~'*50)
print('{} → {} → ' .format(t1, t2), end='')
while i <= n:
    t3 = t1+t2
    print('{} → ' .format(t3), end='')
    i +=1
    t1 = t2
    t2 = t3
print('FIM')
print('~'*50)