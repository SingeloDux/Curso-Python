# Faca um programa que leia duas notas de um aluno e calcule sua media mostrando uma mensagem no final de acordo com a media atingida:
# Media abaixo de 5.0: REPROVADO; Media entre 5.0 e 6.9: RECUPERACAO; Media 7.0 ou superior: APROVADO

print('{:=^50}' .format('CALCULADORA DE MEDIA DO ALUNO'))

n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))

media = (n1+n2)/2

print('Tirando a nota \033[31m{}\033[m e \033[31m{}\033[m, a media do aluno fica \033[31m{}\033[m' .format(n1,n2,media))

if media < 5:
    print('\033[31mREPROVADO\033[m')
elif media >= 5 and media <= 6.9:
    print('\033[33mRECUPERACAO\033[m')
else:
    print('\033[32mAPROVADO\033[m')