'''
Em python, para interromper um laco de repeticao utilizamos o break;
Apartir do Python 3.6 foi implementado o F-Strings, que servem para simplificar o print
'''
num = soma = i = 0

while True:
    num = int(input('Digite um numero inteiro (999 para sair): '))
    if num == 999:
        break
    i+=1
    soma += num
#print('Voce digitou %d numeros e a soma entre eles e %d!' % (i, soma)) #PYTHON 2
#print('\nVoce digitou {} numeros e a soma entre eles e {}! ' .format(i, soma)) #PYTHON 3
print(f'Voce digitou {i} numeros e a soma entre eles e {soma}!') #PYTHON 3.6+

nome = 'Singelo Dux'
salario = soma
print(f'O nome e{nome:-^15} e ganha {salario:.2f}MT')