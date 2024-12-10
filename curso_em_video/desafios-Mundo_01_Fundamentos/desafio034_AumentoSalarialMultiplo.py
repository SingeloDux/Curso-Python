# Faca um programa que pergunte o salario de um funicionario e calcule o valor do seu aumento. Para salarios superiores a 12.500mt, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento e de 15%.

salario = float(input('Informe o salario do funcionario para calcular o seu aumento: '))
print('-_'*30)

if salario <= 12500:
    aumento = salario + (salario*0.15)
    #aumento = salario + (salario*15/100)

else:  
    aumento = salario + (salario*0.10)
    #aumento = salario + (salario*10/100)

print('Quem ganhava {:.2f}MT, passa a ganhar {:.2f}MT.\n' .format(salario, aumento))