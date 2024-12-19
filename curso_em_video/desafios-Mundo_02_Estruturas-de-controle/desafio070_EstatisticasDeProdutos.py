# Crie um programa que leia o nome e o preco de varios produtos. O programa devera perguntar se o usuario vai continuar. No final, mostre:

separador = '-=-'*17
nomeProg = ' LOJA SUPER BARATAO '
print(f'\n\033[1;32m{separador:^50}\n{nomeProg:-^50}\n{separador:^50}\033[m')

total = cont = primeiraEntrada = baratao = 0
resposta = 'S'
while True:

    while resposta == 'S':
        nome = str(input('Nome do Produto: ')).strip().upper()
        preco = float(input('Preco: '))
        primeiraEntrada +=1

        #a) Qual e o total gasto na compra;
        total +=preco
        #b) Quantos produtos custam mais de 1000MT;
        if preco > 1000:
            cont +=1
        #c) QUal e o nome do produto mais barrato;
        if primeiraEntrada == 1 or preco < baratao:
            baratao = preco
            maisBarato = nome

        resposta = str(input('Quer continuar [S/N]?: ')).strip().upper()[0]
        while resposta not in 'SN':
            resposta = str(input('Responda com SIM OU NAO! [S/N]: ')).strip().upper()[0]
    break
print(f'\n======= FIM DO PROGRAMA =======')
print(f'O valor total da sua compra foi: {total:.2f}')
print(f'O total de produtos custando mais de 1000MT e: {cont}')
print(f'O produto mais barrato foi {maisBarato} que custou {baratao:.2f}MT')