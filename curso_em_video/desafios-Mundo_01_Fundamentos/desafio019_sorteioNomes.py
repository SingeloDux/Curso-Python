# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faca um programa que ajude ele, lendo o nome dos alunos e escrevendo o nome do escolhido.
from random import choice

alu01 = input('Insira o nome do primeiro aluno: ')
alu02 = input('Insira o nome do primeiro aluno: ')
alu03 = input('Insira o nome do primeiro aluno: ')
alu04 = input('Insira o nome do primeiro aluno: ')

ListAlunos = [alu01, alu02, alu03, alu04]
escolhido = choice(ListAlunos)

print('--------\nO aluno {} foi escolhido para apagar o quadro!' .format(escolhido))
