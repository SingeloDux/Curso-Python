# Faca um algoritmo que leia o preco de um produto e mostre seu novo preco, com 5% de desconto.

print('='*5, 'Calculadora de desconto dum produto!', '='*5)

preco = float(input('Digite o preco do produto para calcular desconto: '))

novoPreco = preco - (preco * 0.05)
print('O novo preco do produto apos o desconto de 5% e de {:.2f}MT' .format(novoPreco))

# OR THE HARD WAY

novo = preco - (preco*5/100)
print('O novo preco do produto apos o desconto de 5% e de {:.2f}MT' .format(novo))