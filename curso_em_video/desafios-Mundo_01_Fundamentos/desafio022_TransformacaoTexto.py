"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
"""

nome = input('Insira o seu nome para analise: ')

# O nome com todas as letras maiusculas
print(nome.upper())

# O nome com todas as minusculas
print(nome.lower())

# Quantidade de letras ao todo sem considerar espacos
remSpaces = nome.replace(' ', '')
print('Seu nome tem {} letras ignorando os espacos'.format(len(remSpaces)))

# Quantas letras tem o primeiro nome
listaNomes = nome.split()
firstName = len(listaNomes[0])
print('Seu primeiro nome tem {} letras'.format(firstName))
