"""
Em python nao ha declaracao de variaveis, apenas a inicializacao

Apartir do Python 3.6 foi implementado o F-Strings, que servem para simplificar o print

Alinhamento:
> Direita
< Esquerda
^ Centralizado
=^ centralizado preenchido com caracteres = se definido quantidade de espacos Ex: {:=^20}
"""

a = "Ola"
b = " "
c = "Mundo!"
nome = input('Informe o seu nome: ')

#print('\nOla ' +nome+', esse e o primeiro script em python. O famoso: ' +a + b + c)

#print('\nOla %s, esse e o primeiro script em Python. O famoso: %s %s %s' % (nome, a,b,c)) #PYTHON 2
#print('\nOla {}, esse e o primeiro script em Python. O famoso: {}{}{}' .format(nome, a, b, c)) #PYTHON 3
print(f'\nOla {nome}, esse e o primeiro script em Python. O famoso: {a}{b}{c}') #PYTHON 3.6+


