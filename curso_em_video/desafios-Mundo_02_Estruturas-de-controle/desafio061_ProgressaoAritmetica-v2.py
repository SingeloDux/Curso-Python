# Refaca o desafio 051, lendo o primeiro termo e a razao de uma PA, mostrando os 10 primeiros termos da PA usando o while.

print('\n {:=^45}'.format('\033[1m10 TERMOS DUMA PROGRESSAO ARITMETICA \033[m'))

primeiro = int(input('\nDigite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))

termo = primeiro
i = 1
print('\nOs 10 primeiros termos da PA sao: ')

while i <= 10:
        print('{} → ' .format(termo), end='')
        termo +=razao
        i+=1

print('FIM')