# import math - Da seguinte forma importamos todas as funcoes do modulo: ceil, floor, trunc, pow, sqrt, factorial, etc 
"""
import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz quadrada de {:.2f} e igual a {:.2f}' .format(num, math.ceil(raiz)))
"""

# from math import sqrt, ceil - Da seguinte forma importamos apenas importamos a funcao sqrt e ceil, o que ajuda na economia de memoria

#from math import sqrt, ceil
#num = int(input('Digite um numero: '))
#raiz = sqrt(num)
#print('A raiz quadrada de {} e igual a {:.2f}' .format(num, ceil(raiz)))

from random import randint, random
aleatorio = random()
aleatorio2 = randint(1,10)
print('Aleatorio: {}, \nAleatorio de 1 a 10: {}' .format(aleatorio, aleatorio2))

