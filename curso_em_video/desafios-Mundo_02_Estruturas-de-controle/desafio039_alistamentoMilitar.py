# Faca um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# Se ele ainda vai se alistar ao servico militar (17 anos); Se e a hora de se alistar (18 anos); Se ja passou do tempo do alistamento (30 anos);
# Seu programa tambem devera mostrar o tempo que falta ou passou do prazo;
from datetime import date
anoAtual = date.today().year

print('VERIFICA ALISTAMENTO MILITAR!')

anoNasc = int(input('Digite o seu ano de nascimento: '))
idade = anoAtual - anoNasc

if idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    print('Voce ainda e menor de idade, e faltam {} anos para se alistar!' .format(18-idade))
elif idade >18:
    print('Voce ja deveria ter se alistado a {} anos' .format(idade-18))