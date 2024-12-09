# Faca um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informacoes possiveis sobre ele.

print('Este programa recebe dados e informa o tipo primitivo e outras informacoes relevantes dele!')
algo = input('Digite qualquer coisa: ')

print('O tipo primitivo do dado digitado e', type(algo))
print('So tem espacos? ', algo.isspace())
print('E um numero? ', algo.isnumeric())
print('E alfabetico? ', algo.isalpha())
print('E alfanumerico? ', algo.isalnum())
print('Esta em maiusculas? ', algo.isupper())
print('Esta em minusculas? ', algo.islower())
print('Esta capitalizada? ', algo.istitle())
