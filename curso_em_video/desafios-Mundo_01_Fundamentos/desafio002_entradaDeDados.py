"""
EXERCICIO 1
Faca um formulario que capture do usuario os segunites dados:
- Nome, Altura, Idade, Telefone
Depois imprima em um relatorio organizado
"""
nome = input("Insira o seu nome: ")
altura = input("Insira a sua altura: ")
idade = input("Informe a sua idade: ")
celular = input("Informe o seu numero de celular: ")

print("\n=================== RELATORIO FINAL ===================")
# print("Eu", nome, "de", idade, "de idade, apenas fiz esse relatorio \npara provar a mim mesmo que o exercicio proposto e muito facil. \nA minha altura e de", altura+"m e o meu contacto e:", celular)

print('Eu {} de {} anos de idade, apenas fiz esse relatorio \npara provar a mim mesmo que o exercicio proposto e muito \nfacil. A minha altura e de {}m e o meu contacto e {}' .format(nome, idade, altura, celular))

print("========================== FIM ==========================")