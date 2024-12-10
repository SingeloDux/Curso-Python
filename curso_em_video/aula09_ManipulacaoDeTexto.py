frase = 'Curso Basico de Pyth0n'
print(frase)

print('FATIAMENTO DE STRINGS: Var[index:range:saltos]')
print('*'*20 +'\n')
print('frase[3] pega o 3o char: ', frase[3])
print('frase[3:15] peaga chars de 3 a 14: ', frase[3:15])
print('frase[:15] pega de 0 a 14: ', frase[:15])
print('frase[15:] pega de 15 ate o fim: ', frase[15:])
print('frase[5::3] pega de 3 ate o final, pulando de 3 em 3: ', frase[5::3])
print('frase[5:15:3] pega de 3 ate 14 pulando de 3 em 3: ', frase[5:15:3])
print('frase[::3] salto de 3 em 3: ', frase[::3])

print('*'*20 +'\n')
print('ANALISE DE STRINGS')
print('Tamanho/Length da frase  : ', len(frase))
print('Contagem de todos os <o> : ', frase.count('o'))
print('Contagem c/ fatiamento 0-12: ',frase.count('o', 0, 13))
print('Localizar trecho na frase: ', frase.find('de'))
print('Localizar trecho inexistente: ', frase.find('Cyber'))
print('Curso' in frase)
print('Android' in frase)


print('*'*20 +'\n')
print('TRANSFORMACAO DE STRINGS')
print('Fazendo REPLACE de  Pyth0n: ', frase.replace('Pyth0n', 'Phyton') )

frase2 = '  Curso Basico de Pyth0n  '
print('NOVA FRASE:', frase2)
print('Removendo espacos c/ STRIP:', frase2.strip())
print('Removendo espacos c LSTRIP:', frase2.lstrip())
print('Removendo espacos c RSTRIP:', frase2.rstrip())
print('Aplicando o UPPER na frase: ', frase.upper())
print('Aplicando o LOWER na frase: ', frase.lower())
print('Aplicando o LOWER na frase: ', frase.lower())
print('Aplicando o CAPITALIZE ...:', frase.capitalize())
print('Aplicando o TITLE na frase:', frase.title())
print('Dividindo a frase c/ SPLIT: ', frase.split())
print('Juntando a frase com JOIN : ','-'.join(frase))

print("""
The Brown Fox,
Jumps over the white rabbit
And, I forgot The Font Story Installation
But Now We Know How To Write Paragraphs
""")