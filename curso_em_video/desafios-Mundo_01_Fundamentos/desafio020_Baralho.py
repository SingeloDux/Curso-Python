# O mesmo professor do desafio anterior quer sortear a ordem de apresentacao de trabalhos dos alunos. Faca um programa que leia o nome dos quatro alunos e moste a ordem sorteada.
from random import shuffle

alu01 = input('Insira o nome do primeiro aluno: ')
alu02 = input('Insira o nome do primeiro aluno: ')
alu03 = input('Insira o nome do primeiro aluno: ')
alu04 = input('Insira o nome do primeiro aluno: ')

ListAlunos = [alu01, alu02, alu03, alu04]
shuffle(ListAlunos)

print('===== Resultado do sorteio =====')
print('Os alunos apresentarao o trabalho na seguinte ordem {}!' .format(ListAlunos))
