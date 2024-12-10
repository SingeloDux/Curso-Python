''' 
Faca um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados. 
Ex: Digite um numero: 1834
unidade: 4 | dezena: 3 | Centena: 8| milhar: 1
'''

num = int(input('Digite um numero de 0-9999 para analise: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o numero {}, o programa identificou o: ' .format(num))
print('{} como Unidade' .format(u))
print('{} como Dezena' .format(d))
print('{} como Centena' .format(c))
print('{} como Milhar' .format(m))

''' 
nr = str(num)
print('{} como Unidade' .format(nr[3]))
print('{} como Dezena' .format(nr[2]))
print('{} como Centena' .format(nr[1]))
print('{} como Milhar' .format(nr[0]))
'''