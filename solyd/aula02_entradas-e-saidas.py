'''
O print pode ser usado com aspas duplas ou simples!
O input sempre retorna um objeto do tipo string
'''
print('===================== Entradas E De Dados =====================')

gamer_id = 324
# nome = input("Informe o seu nome para obter teu score:  ")
nome = "Singelo Dux"
pontos = 22.1

# As virgulas e as aspas da concatenacao estao aparecendo estao aparecendo
print('===============================================================')
print('Gamer ID \t Nome \t Pontos ')
print(gamer_id, "\t\t", nome, "\t", pontos)
print(type(gamer_id), "\t", type(nome), "\t", type(pontos))

# Concatenacao com mais exige a conversao de variaveis para string e insercao de espacos manualmente
print('\n=============================================================')
print('Gamer ID \t Nome \t Pontos ')
print(str(gamer_id) + '\t' + nome + '\t' + str(pontos))

tipos_variaveis = type(gamer_id), type(nome), type(pontos)
print(tipos_variaveis)
print('\n=============================================================')
