# Faca um programa que leia um ano qualquer e mostre se ele e BISSEXTO. Sabendo que:
# Um ano bissexto e um ano que tem um total de 366 dias, isto e, um dia a mais que os anos comuns de 365 dias.
# Esse fenomeno ocorre a cada 4 anos, excepto anos multiplos de 100 que nao sao multiplos de 400
from datetime import date

ano = int(input('Digite um ano para saber se e um ano BISSEXTO (Digite 0 para o ano atual): '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('O ano {} e BISSEXTO!' .format(ano))
else:
    print('O ano {} nao e BISSEXTO!' .format(ano))
