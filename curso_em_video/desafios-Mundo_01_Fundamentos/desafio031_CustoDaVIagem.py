# Desenvolva um programa que pergunte a distancia da viagem em KM. Calcule o preco da passagem, cobrando 1mt por KM para viagens de ate 200KM e 0.80 para viagens mais longas.

dist = float(input('Qual a distancia estimada da sua viagem? : '))

print('\nVoce esta prestes a iniciar uma viagem de {:.1f}Km.'.format( dist))
print('*'*50)

#bilhete = dist*1 if dist<=200 else dist * 0.80

if dist <= 200:
    bilhete = dist*1
else:
    bilhete = dist*0.80

print('O preco da sua passagem sera de {:.2f}MT\n'.format(bilhete))