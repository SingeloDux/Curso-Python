# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Singelo" no nome.

nome = input('Digite o seu nome completo para analise: ').strip()

# verifica = 'SINGELO' in nome.upper()
#print('Singelo esta em seu nome? :', verifica)

print('Singelo esta em seu nome? : {}' .format('SINGELO' in nome.upper()))

