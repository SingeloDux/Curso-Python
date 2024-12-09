# Faca um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento.

print('='*5, 'Calculadora de aumento salarial!', '='*5)

salario = float(input('Digite o salario atual do funcionario: '))

novoSal = salario + (salario*0.15)

print('Apos o aumento de {:.2f}MT correspondente a 15%, o funcionario passara a receber {:.2f}MT' .format(salario*0.15, novoSal))