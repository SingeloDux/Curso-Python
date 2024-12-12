# Lacos, Repeticoes ou Iteracoes

# Contagem Normal Usando For
for i in range (0,6):
    print(i, end=', ')
print('\n')

# Contagem Com Salto Usando For
for i in range (0, 12, 2): # comeca no 0 e faz saltos de 2 
    print(i, end=', ')
print('\n')

# Contagem Regressiva Usando For
for i in range (6, 0, -1): # comeca no 6 e tira 1
    print(i, end=', ')
print('\n')

start = int(input('Digite o inicio do intervalo: '))
end = int(input('Digite o fim do intervalo: '))
jump = int(input('Digite o nr de saltos de contagem: '))

for i in range (start, end, jump):
    print(i, end=', ')
print('\n')