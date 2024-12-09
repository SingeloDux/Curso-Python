'''
Operadores Aritmeticos e sua ordem de precedencia
1 - () Parentesis, obvio que nao e um operador :-)
2 - Potencia **
3 - Multiplicacao *, Divisao /, Divisao Inteira // (5//2=2), Resto da Divisao % (5%2=1)
4 - Adicao +, Subtracao -

Uso: Operando1 Operador Operando2 Atribuicao Resultado
'''
n1 = int(input('Digite o valor um: '))
n2 = int(input('Digite o valor dois: '))

soma = n1+n2
subt = n1-n2
mult = n1*n2
divi = n1/n2
divt = n1//n2
rdiv = n1%n2
pot = n1**n2

#print('Os numeros digitados foram {} e {} e tem como resultados: \nSoma: {}\nSubtracao: {} \nProduto: {} \nQuociente: {}\nDivisao Inteira: {}\nResto da Divisao: {:.2f}\nPotenciacao: {}' .format(n1, n2, soma,subt,mult,divi,divt,rdiv,pot))

print('Os numeros digitados foram {} e {} e tem como resultados: ' .format(n1, n2), end = ' ')

print('\nSoma: {}\nSubtracao: {} \nProduto: {} \nQuociente: {}\nDivisao Inteira: {}\nResto da Divisao: {:.2f}\nPotenciacao: {}' .format(soma,subt,mult,divi,divt,rdiv,pot))