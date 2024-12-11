# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Qual e o valor da casa?: '))
salario = float(input('Qual o salario do comprador?: '))
anos = float(input('Em quantos anos o comprador vai pagar a casa?: '))

parcMensal = valor/(anos*12)

if parcMensal > salario * 30/100:
    print('\033[31mEMPRESTIMO RECUSADO \nA prestação mensal de {:.2f} excede 30% do seu salário!\033[m' .format(parcMensal))
elif parcMensal <= salario * 30/100:
    print('\033[32mEMPRESTIMO APROVADO \nA sua prestação mensal sera {:.2f}MT!\033[m' .format(parcMensal))

print('\nFIM')