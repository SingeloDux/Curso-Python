# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preco a pagar sabendo que o carro custa 60Mt por dia e 0.15 por km rodado.

dias = int(input('Quantos dias alugados? >>> '))
dist = float(input('Quantos KM rodados? >>> '))
valor = (dias*60) + (dist*0.15)

print('O total a pagar e de {:.2f}MT' .format(valor))