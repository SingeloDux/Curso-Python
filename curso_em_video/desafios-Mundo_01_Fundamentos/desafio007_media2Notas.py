# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua media.

print('='*5, 'Calculadora de Media', '='*5)

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1+nota2)/2

print('A media do aluno com as notas {:.2f} e {:.2f}, e de {:.2f} valores! ' .format(nota1, nota2, media))

#A linguagem python aceita acentuacoes em variaveis