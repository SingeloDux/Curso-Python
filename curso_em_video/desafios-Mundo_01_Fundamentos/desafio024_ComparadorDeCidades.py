# Crie um programa que leia o nome de uma cidade e diga se ela comeca ou nao com o nome "Cabo".

cidade = input('Digite o nome duma cidade para analise: ')

#verify = 'Cabo' in cidade[0:4]
#print('O nome da sua cidade comeca com Cabo? : ', verify )

print('O nome da sua cidade comeca com Cabo? : {} ' .format(cidade[0:4] == 'Cabo') )
print('O nome da sua cidade comeca com Cabo? : {} ' .format('Cabo' in cidade[0:4]) )