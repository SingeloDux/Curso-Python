''' 
Estrutura de repeticao com teste logico

Existem alguns casos onde o laco de repeticao FOR nao funciona, isso porque so podemos usar o FOR 
quando sabemos o limite...isto e, vai de inicio ate o fim;

Quando nao sabemos o limite, usamos o WHILE, que executara "Enquanto" nao chegar ao objetivo

Entenda que: Nao existe a estrutura mais rapida entre o FOR e o WHILE, no entanto quando sabemos o 
limite, o FOR e o mais pratico. E o WHILE pode ser utilizado para ambas as situacoes;
'''
# CONTAGEM DE 1 A 10 USANDO FOR
for i in range (1,10):
    print(i)

#  MESMO EXEMPLO COM WHILE, POREM COM MAIS LINHAS
i = 1
while i < 10:
    print(i)
    i +=1

# Exemplo: Leia a idade de todas as pessoas que entrarem no BAR! Nao da pra saber quantas pessoas! Logo:
resposta = 'S'
while resposta == 'S':
    idade = int(input('Digite a idade da pessoa: '))
    resposta = str(input('Ainda tem pessoas para verificar a idade? [S/N]')).upper()
print('FIM DO PROGRAMA')

num = 1
par = impar = 0
while num != 0:
    num = int(input('Digite um numero: '))

    if num != 0: 
        if num % 2 == 0:
            par +=1
        else:
            impar +=1
print('VOCE DIGITOU {} PARES E {} IMPARES!' .format(par, impar))
