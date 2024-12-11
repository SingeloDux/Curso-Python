# Assim como nas estruturas simples/compostas, em estruturas aninhadas, o uso do else e opcional. Isto e, a estrutura pode terminar com if ou elif
# Podemos usar quantos elif quisermos

nome = str(input('Ola humano, qual e o seu nome?: '))

if nome == 'Singelo':
    print('Oi mestre, desculpe a minha petulância!')
elif nome == 'Singelo Dux' or nome == 'Dux':
    print('Oi mestre, desculpe a minha petulância!')
elif nome in 'Eduardo Edu Dudu':
    print('Oi mestre, desculpe a minha petulância!')
else:
    print('Ola {}, o que traz voce ao palacio dos Deuses?'.format(nome))
print('\nFIM')