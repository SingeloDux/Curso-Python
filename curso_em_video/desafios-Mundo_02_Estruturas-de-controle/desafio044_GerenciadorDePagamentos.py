# Elabora um programa que calcule o valor a ser pago por um produto, considerando o seu preco normal e a condicao do pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal 
# 3x ou mais no cartão: 20% de juros

print('\033[1;34mCAIXA REGISTRADORA\033[m\n', '=-'*22)

preco = float(input('Qual o preco das compras: '))

print('=-'*30)
print('METODO DE PAGAMENTO \n1 - à vista dinheiro/cheque \n2 - à vista no cartão \n3 - em até 2x no cartão \n4 - 3x ou mais no cartão')
print('=-'*30)

opcao = int(input('Digite a opcao: '))

if opcao == 1:
    total = preco - (preco*10/100)
elif opcao == 2:
    total = preco - (preco*5/100)
elif opcao == 3:
    total = preco
    parcela = total/2
    print('Sua compra sera parcelada em 2x de {:.2f}MT SEM JUROS' .format(parcela))
elif opcao == 4:
    total = preco + (preco*20/100)
    totalPar = int(input('Quantas parcelas? : '))
    parcela = total/totalPar
    print('Sua compra sera parcelada em {}x de {:.2f}MT COM JUROS' .format( totalPar, parcela))
else:
    total = preco
    print('\033[31mErro: Opcao Invalida!')

print('Sua compra de \033[32m{:.2f}MT\033[m vai custar \033[32m{:.2f}MT\033[m no final!' .format(preco, total))
