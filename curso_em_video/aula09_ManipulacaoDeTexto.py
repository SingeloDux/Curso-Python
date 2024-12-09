# Frase = 'String = Cadeia de Text0'

# Fatiamento de string: Varialvel+Indice ou Range Ex: 

frase = 'Curso Basico de Python'
print('Fatiamento de string: Varialvel+Indice ou Range')
print('Frase: ', frase)
print('frase[3] pega o 3o char: ', frase[3])
print('frase[3:15] peaga chars de 3 a 14: ', frase[3:15])
print('frase[:15] pega de 0 a 14: ', frase[:15])
print('frase[15:] pega de 15 ate o fim: ', frase[15:])
print('frase[5::3] pega de 3 ate o final, pulando de 3 em 3: ', frase[5::3])
print('frase[5:15:3] pega de 3 ate 14 pulando de 3 em 3: ', frase[5:15:3])
print('frase[::3] salto de 3 em 3: ', frase[::3])

# Analise: 
# Tamanho da frase: len(frase)
# Contador de char: frase.count('a') ou frase.count('a', 0, 13)-contagem c/ fatiamento de 0 a 12
# Localizar: frase.find('de') se retornar -1 significa que nao existe // 'Cadeia' in frase - retorna true or false

# Transformacao
# Replace: frase.replace('Text0', 'Texto')
# Maiusculas, Minusculas: frase.upper(), frase.lower() - substitui o que nao esta de acordo com o metodo
# Capitalizar: frase.capitalize() - Apenas a primeira letra da frase fica maiuscula
# Title: frase.title() - Faz capitalize de todas as primeiras letras apos os espacos
# STRIP: frase.strip() - remove os espacos excessivos no inicio e no final da string | ao usar rstrip ou lstrip, removemos apenas os espacos da direita ou esquerda.
# Divisao: frase.split() - Divide a frase em palavras apos os espacos, criando uma lista de strings
# Juncao: '-'.join(frase) - Junta strings adicionando o caratere informado na funcao

