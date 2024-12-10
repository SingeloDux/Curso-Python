# Faca um programa que leia uma frase pelo teclado e mostre:

frase = str(input('Digite uma frase qualquer para analise: ')).strip().upper()

#Quantidade de vezes que aparece a letra "A"
print('A leta <A> aparece {} vezes na sua frase!' .format(frase.count('A')))

# Em que posicao ela aparece pela primeira vez
print('A leta <A> aparece pela primeira vez na posicao {} ' .format(frase.find('A')+1))

# Em que posicao ela aparece pela ultima vez
print('A leta <A> aparece pela ultima vez na posicao {} ' .format(frase.rfind('A')+1))
