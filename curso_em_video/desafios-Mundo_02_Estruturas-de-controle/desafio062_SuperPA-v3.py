#Melhore o desafio 061, perguntando para o usuario se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

print('\n {:=^45}'.format('\033[1m 10 TERMOS DUMA PROGRESSAO ARITMETICA \033[m'))

primeiro = int(input('\nDigite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))

i = 1
termo = primeiro
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while i <= total:
            print('{} → ' .format(termo), end='')
            termo +=razao
            i+=1
    print('PAUSA')
    mais = int(input('\nQuantos termos voce quer mostrar a mais? (0 - Nenhum): '))
print('\nPA finalizada com {} termos exibidos!' .format(total))