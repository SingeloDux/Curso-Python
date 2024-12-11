#  Refaca o desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado"
# Equilatero: todos lados iguais
# Isosceles: dois lados iguais
# Escaleno: todos os lados diferentes

print('\033[1;34mVERIFICADOR DE RETAS PARA FORMAR TRIANGULO\033[m\n', '=-'*22)
r1 = float(input('Digite o comprimento da recta 1: '))
r2 = float(input('Digite o comprimento da recta 2: '))
r3 = float(input('Digite o comprimento da recta 3: '))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('Os segmentos informados PODEM FORMAR um triangulo ', end='')
    if r1 == r2 == r3:
        print('EQUILATERO!')
    if r1 != r2 != r3:
        print('ESCALENO!')
    else:
        print('ISOSCELES!')
else:
    print('Os segmentos informados NAO PODEM FORMAR um triangulo!')