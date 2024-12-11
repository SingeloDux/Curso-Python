# A confederacao Nacional de Natacao precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Ate 9anos: MIRIM
#Ate 14 anos: Infantil
#Ate 19 anos: Junior
#Ate 20 anos: Senior
# Acima: Master
from datetime import date
ano = date.today().year
print('{:=^50}' .format('CONFEDERACAO NACIONAL DE NATACAO'))

anoNasc = int(input('Digite a sua idade para saber sua categoria: '))
idade = ano - anoNasc

print('O atleta tem {} anos!' .format(idade))
if idade <=9:
    print('Classificacao: MIRIM!')
elif idade >9 and idade<=14:
    print('Classificacao: INFANTIL!')
elif idade > 14 and idade <=19:
    print('Classificacao: JUNIOR!')
elif idade > 19 and idade <=20:
    print('Classificacao: SENIOR!')
else:
    print('Classificacao: MASTER!')