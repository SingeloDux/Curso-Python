# Por padrao o input captura valores do tipo string. Dessa forma podemos capturar os valores e convertelos em inteiros ou qualquer outro tipo de dado: float, bool, etc

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
soma = n1 + n2
#print('A soma entre',n1,'e',n2, 'vale ', soma)
print('A soma entre {} e {} vale {}'.format(n1, n2, soma))

# Existem metodos de teste de dados:
n = input('Digite qualquer coisa: ')
print(n.isnumeric()) #Verifica se e um numero e retorna True or False Ex: 7
print(n.isalpha()) #Verifica se e uma letra e retorna True or False Ex: a
print(n.isalnum()) #Verifica se e alfanumerico e retorna True or False Ex: 3a
print(n.isupper()) #Verifica se e maiusculo, poderia ser islower para minisculo