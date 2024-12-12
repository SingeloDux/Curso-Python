# Crie um programa que calcule a soma entre todos os numeros impares que sao multiplos de tres e que se encontram no intervalo de 1 ate 500

print('\n {:=^45}'.format('\033[1m SOMADOR DE NRs IMPARES \033[m'))

soma = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        #print(i, end=' + ')
        soma += i
        cont +=+1

print('\nA SOMA DE TODOS OS {} VALORES IMPARES E IGUAL: {} ' .format( cont , soma))