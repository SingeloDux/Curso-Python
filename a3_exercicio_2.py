# True or False
# Comparadores: > >= == != <= < and or not
'''
Exercicio
 Faca um programa que pergunte a idade, o peso e a altura de uma pessoa e decide se ela esta apta aser do exercito.
 Para entrar no exercito e preciso:
 - Pesar mais ou igual 60kilos
 - Medir mais ou igual 1,70m
 - Ter mais ou igual18 anos
'''
print('Este programa tem como objectivo verificar se voce esta apto a entrar no exercito ou nao. \nEntao, por favor informe os seus dados verdadeiros abaixo para verificacao.')
idade = input('Quantos anos voce tem? \n>>>:')
peso = input('Quantos quilogramas voce pesa? \n>>>:')
altura = input('Qual a sua altura? \n>>>:')

if idade >= 18 or peso >= 60 or altura >= 1.70 == True:
    print('Parabes! Voce esta apto a entrar no exercito.')
else:
    print('Sentimos muito, voce nao cumpre os requisitos para fazer parte do exercito.')
