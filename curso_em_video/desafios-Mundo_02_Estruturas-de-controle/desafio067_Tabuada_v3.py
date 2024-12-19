# Faca um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario. O programa sera interrompido quando o numero solicitado for negativo.

print('\n\033[1;32m{}{:^20}{}\033[m' .format('-='*8,'GERADOR DE TABUADA','-='*8))

while True:
    n = int(input('Qual numero deseja ver sua tabuada? : '))
    print('~'*40)
    if n < 0:
        break
    for i in range(1, 13):
        print(f'{n} x {i:2} = {n*i:2}')
    print('~'*40)
print('\nGERADOR DE TABUADA ENCERRADO! OBRIGADO POR USAR O PROGRAMA!')   