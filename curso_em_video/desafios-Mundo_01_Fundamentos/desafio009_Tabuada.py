# Faca um programa que leia um numero e mostre na tela a sua tabuada

print('='*5, 'Tabuada de um numero', '='*5)

num = int(input('Digite um numero para ver a sua tabuada: '))
print('-'*12)

# print(' {} * 1 = {}\n {} * 2 = {}\n {} * 3 = {}\n {} * 4 = {}\n {} * 5 = {}\n {} * 6 = {}\n {} * 7 = {}\n {} * 8 = {}\n {} * 9 = {}\n {} * 10 = {}\n {} * 11 = {}\n {} * 12 = {}\n' .format(num, num*1, num, num*2, num, num*3, num, num*4, num, num*5, num, num*6, num, num*7,num, num*8, num, num*9,num, num*10,num, num*11, num, num*12))

print('{} x {:2} = {}' .format(num, 1, num*1))
print('{} x {:2} = {}' .format(num, 2, num*2))
print('{} x {:2} = {}' .format(num, 3, num*3))
print('{} x {:2} = {}' .format(num, 4, num*4))
print('{} x {:2} = {}' .format(num, 5, num*5))
print('{} x {:2} = {}' .format(num, 6, num*6))
print('{} x {:2} = {}' .format(num, 7, num*7))
print('{} x {:2} = {}' .format(num, 8, num*8))
print('{} x {:2} = {}' .format(num, 9, num*9))
print('{} x {:2} = {}' .format(num, 10, num*10))
print('{} x {:2} = {}' .format(num, 11, num*11))
print('{} x {:2} = {}' .format(num, 12, num*12))
print('-'*12)
3