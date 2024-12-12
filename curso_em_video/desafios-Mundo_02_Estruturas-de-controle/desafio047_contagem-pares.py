# Crie um programa que mostre na tela todos os numeros pares no intervalo de 1 e 50

print('\nNUMEROS PARES ENTRE 1 e 50!')
print('-='*48)

for i in range(2, 51, 2):
    print(i, end=' ')
print('\n', '-='*48)
print('FIM DO PROGRAMA!')

'''consome mais recursos porque executa iteracoes extras, mesmo que nao exibidas.
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=' ')
print('\n', '-='*48)
print('FIM DO PROGRAMA!')
'''