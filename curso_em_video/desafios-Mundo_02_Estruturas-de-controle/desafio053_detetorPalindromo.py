# Crie um programa que leia uma frase qualquer e diga se ela e um palindromo, desconsiderando os espacos. Saiba que: Palindromo sao palvras que podem ser lidas de tras para frente ou de frente para tras do mesmo jeito. Ex: Ana, Apos A Sopa, A sacada da casa, A torre da derrota, O lobo ama o bolo, anotaram a data da maratona, etc


print('\n {:=^45}'.format('\033[1m VERIFICADOR DE PALINDROMOS \033[m'))

frase = str(input('\nDigite uma frase qualquer: ')).strip().upper()
palavras = frase.split()
noSpace = ''.join(palavras)
inverso = ''
# inverso = noSpace[::-1] # fazer o inverso sem o for
for letra in range(len(noSpace) -1, -1, -1):
    inverso += noSpace[letra] 

print('O inverso de \033[32m{}\033[m e \033[33m{}\033[m ' .format(frase, inverso))
if inverso == noSpace:
    print('\033[33mA frase digitada e um palindromo!\033[m')
else:
    print('\033[31mA frase digitada NAO e um palindromo!\033[m')

