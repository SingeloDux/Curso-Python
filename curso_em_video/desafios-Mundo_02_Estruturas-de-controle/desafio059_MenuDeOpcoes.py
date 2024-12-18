''' 
Crie um programa que leia dois valores e mostre um menu na tela:

[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Numeros
[5] Sair do programa

Seu programa devera realizar a operacao solicitada em cada caso!
'''
print('\n {:=^45}'.format('\033[1;33m CALCULADORA \033[m'))

n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
opcao = 0
while opcao != 5:
    print("""
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Numeros
    [5] Sair do programa """)
    opcao = int(input('Escolha uma das opcoes (1 a 5): '))

    if opcao == 1:
        soma = n1 + n2
        print('A soma de {} e {} e igual a {}!' .format(n1,n2,soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O produto de {} e {} e igual a {}!' .format(n1,n2,produto))
    elif opcao == 3:
        if n1 > n2:
            print('Entre {} e {} o maior e {}' .format(n1, n2, n1))
        elif n2 > n1:
            print('Entre {} e {} o maior e {}' .format(n1, n2, n2))
        else:
            print('{} e {} sao IGUAIS' .format(n1,n2))
    elif opcao == 4:
        n1 = float(input('Digite o primeiro numero: '))
        n2 = float(input('Digite o segundo numero: '))
    elif opcao == 5:
        print('\nObrigado por usar o programa!')
    else:
        print('\033[31mErro! A opcao escolhida nao existe\033[m')
    print('-=-='*10)
print('FIM')