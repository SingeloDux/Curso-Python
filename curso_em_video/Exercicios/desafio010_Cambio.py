# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar. COnsidere USD 1 = 63.30Mt

print('='*5, 'Conversor de Moedas', '='*5)

metical = float(input('Digite seu dinheiro em meticais para saber quantos dolares podes comprar: '))

compra = metical/63.30

print('\nCom {:.2f}MT, voce pode comprar US${:.2f} !' .format(metical, compra))