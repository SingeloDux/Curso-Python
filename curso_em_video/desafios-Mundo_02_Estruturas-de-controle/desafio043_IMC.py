# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida 

print('\033[1;34mCALCULADORA DE IMC\033[m\n', '=-'*22)

peso = float(input('Informe o peso em kilogramas: '))
altura = float(input('Informe a alturam em metros: '))
imc = peso / (altura ** 2)

print('O IMC da pessoa e de {:.1f} !' .format(imc))

if imc < 18.5:
    print('Voce esta abaixo do peso NORMAL!')
elif 18.5 <= imc < 25: 
    print('PARABENS, voce esta na faixa de peso NORMAL.')
elif 25 <= imc < 30:
    print('Voce esta em SOBREPESO.')
elif 30 <= imc < 40:
    print('Voce esta em OBESIDADE.')
elif imc >=40:
    print('Voce esta em OBESIDADE morbida, cuidado!.')