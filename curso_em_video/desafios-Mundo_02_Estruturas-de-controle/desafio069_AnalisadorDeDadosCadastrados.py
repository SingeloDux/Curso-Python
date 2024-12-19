# Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa devera perguntar se o usuario quer ou nao continuar. No final, mostre:

separador = '-=-'*17
nomeProg = ' CADASTRO E ANDALISE DE DADOS PESSOAIS'
print(f'\n\033[1;32m{separador:^50}\n{nomeProg:-^50}\n{separador:^50}\033[m')

resposta = 'S'
pessoasM18 = homens = mulheresM20 = 0
while True:
    while resposta == 'S':
        idade = int(input('Digite a idade: '))
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
        while sexo not in 'MF':
            sexo = str(input('Por favor, digite Masculino ou Feminino [M/F]: ')).strip().upper()[0]

        #a) quantas pessoas tem mais de 18 anos
        #b) quantos homens foram cadastrados
        #c) quantas mulheres tem menos de 20 anos
        if idade > 18:
            pessoasM18 +=1
        if idade < 20 and sexo == 'F':
            mulheresM20 +=1
        if sexo == 'M':
            homens +=1
        
        resposta = str(input('Deseja continuar com o cadastro? [S/N]: ')).strip().upper()[0]
        while resposta not in 'SN':
            resposta = str(input('Por favor, digite SIM ou NAO [S/N]: ')).strip().upper()[0]
    break
print(f'\n======= FIM DO PROGRAMA =======')
print(f'Total de pessoas com mais de 18 anos..: {pessoasM18}')
print(f'Total de homens cadastrados no sistema: {homens}')
print(f'Total de mulheres com menos de 20 anos: {mulheresM20}')