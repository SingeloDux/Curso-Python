# Escreva um programa que leia um numero inteiro qualquer e peca para o usuario escolher qual sera a base de conversao: 1 para binario, 2 para octal e 3 para hexadecimal


num = int(input('Informe um numero qualquer para converter para binario, octal ou hexadecimal: '))

print('=-'*30)
print('ESCOLHA A BASE DE CONVERSAO \n1 - BINARIO \n2 - OCTAL \n3 - HEXADECIMAL')
print('=-'*30)

opcao = int(input('Digite a opcao: '))

if opcao == 1:
    print('CONVERTENDO PARA BINARIO...')
    print('O numero \033[32m{}\033[m equivale a \033[32m{}\033[m em binario' .format(num, bin(num)[2:]))
elif opcao == 2:
    print('CONVERTENDO PARA OCTAL...')
    print('O numero \033[33m{}\033[m equivale a \033[33m{}\033[m em octal' .format(num, oct(num)[2:]))
elif opcao == 3:
    print('CONVERTENDO PARA HEXADECIMAL...')
    print('O numero \033[34m{}\033[m equivale a \033[34m{}\033[m em hexadecimal' .format(num, hex(num)[2:]))
else:
    print('\033[31mErro: Opcao Invalida!')

