# Desenvolva um programa que leia seis numeros interiros e mostre a soma apenas daqueles que forem pares. Se o valor for impar, desconsidere-o.

print('\n {:=^45}'.format('\033[1m SOMADOR DE NRs PARES \033[m'))

soma = 0
cont = 0
for i in range(0, 6):
    num = int(input('Digite o {}o numero: ' .format(i+1)))

    if num % 2 == 0:
        soma +=num
        cont +=1
print('\nA soma dos {} numeros PARES digitados e igual a: {}' .format(cont, soma))

