# Refaca o desafio 009, mostrando a tabuada de um numero que o usuario escolher, so que agora utilizando um laco for;

print('\n {:=^45}'.format('\033[1m TABUADA DE UM NUMERO \033[m'))

num = int(input('\nDigite um numero para ver a sua tabuada: '))
print('-'*50)

for i in range (1, 13):
    print('{} x {:2} = {}' .format(num, i, num*i))
print('-'*45)
