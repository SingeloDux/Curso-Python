# Faca um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
# A media da idade do grupo // Qual o nome do homem mais velho// Quantas mulheres tem menos de 20 anos

print('\n {:=^45}'.format('\033[1m ANALISE DE DADOS PESSOAIS \033[m'))
somaIdade = 0
mediaIdade = 0
maisVelhorHomem = 0
nomeMaisVelho = ''
mulheresDe20 = 0

for i in range(1,5):
    print('=-=-=-= {}a PESSOA -=-=-=-='.format(i))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [m/f]: ')).strip()
    somaIdade += idade

    if i == 1 and sexo in 'Mm':
        maisVelhorHomem = idade
        nomeMaisVelho = nome
    if sexo in 'Mm' and idade > maisVelhorHomem:
        maisVelhorHomem = idade
        nomeMaisVelho = nome
    if sexo in 'Ff' and idade < 20:
        mulheresDe20 +=1
mediaIdade = somaIdade/4

print('A media de idade do grupo e de {} anos' .format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {} !' .format(maisVelhorHomem, nomeMaisVelho))
print('Ao todo sao {} mulheres com menos de 20 anos!' .format(mulheresDe20))