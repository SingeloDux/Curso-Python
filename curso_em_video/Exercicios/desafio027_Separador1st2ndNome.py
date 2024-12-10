# Faca um programa que leia o nome completo de uma pessoa, e mostre de seguida o primeiro e o ultimo nome separadamente: Ex: Singelo Dux // primeiro = Singelo | ultimo = Dux

texto = str(input('Digite o seu nome completo para analise: ')).strip()

nome = texto.split()

print('Ola! Prazer em te conhecer!')
print('Seu primeiro nome e: {}' .format(nome[0]))
print('Seu ultimo nome e: {}' .format(nome[len(nome)-1]))