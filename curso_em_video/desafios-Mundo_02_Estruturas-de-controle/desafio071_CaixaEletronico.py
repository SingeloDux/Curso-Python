# Crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergunte o usuario qual sera o valor a ser sacado (numero inteiro) e o programa vai informar quantas notas de cada valor serao entregues. OBS: Considere  que o caixa possui notas de 100MT, 200MT, 500MT E 1000MT;

separador = '-=-'*17
nomeProg = ' BANCO VS CODE '
print(f'\n\033[1;32m{separador:^50}\n{nomeProg:-^50}\n{separador:^50}\033[m')
print(f'\033[1;32mNOTAS DISPONIVEIS: 100MT, 200MT, 500MT, 1000MT\033[m')

valor = int(input('\nQuanto deseja levantar (MT): '))
total = valor
nota = 1000
totalNotas = 0 

while True:
    if total % 100 == 0:
        if total >= nota:
            total -= nota
            totalNotas +=1
        else:
            if totalNotas > 0:
                print(f'Total de {totalNotas} notas de {nota}MT')
            if nota == 1000:
                nota = 500
            elif nota == 500:
                nota = 200
            elif nota == 200:
                nota = 100
            totalNotas = 0
            if total == 0 :
                break    
    else:
        print('\nPor favor informe um valor multiplo de 100MT!')
        break    
print('Obrigado por nos escolher! Volte sempre!\n')