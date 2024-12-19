# Faca um programa que jogue PAR ou Impar com o computador. O jogo so sera interrompido quando o jogador PERDER, mostrando o TOTAL de vitorias consecutivas que ele conquistou no final do jogo.
from random import randint

separador = '-=-'*17
jogo_tres = ' VAMOS JOGAR PAR OU IMPAR '
print(f'\n\033[1;32m{separador:^50}\n{jogo_tres:-^50}\n{separador:^50}\033[m')
vitorias = cpu = 0
while True:
    valor = int(input('Diga um valor ✊: '))
    computador = randint(0,5)
    soma = valor + computador

    jogador = ' '
    while jogador not in 'IP':
        jogador = str(input('Qual sua escolha PAR OU IMPAR [P/I]: ')).strip().upper()[0]

    print(f'Voce jogou {valor} e o computador {computador}. Total igual {soma}, ou seja vence ', end='')
    print('PAR!' if soma % 2 == 0 else 'IMPAR!')

    if jogador == 'P':
        if soma % 2 == 0:
            print('\n\033[32mVoce VENCEU! VAMOS MAIS UMA VEZ!\033[m')
            vitorias +=1
        else:
            print('\n\033[31mVOCE PERDEU! \033[m ')
            cpu +=1
            break
    elif jogador == 'I':
        if soma % 2 == 1:
            print('\n\033[32mVoce VENCEU! VAMOS MAIS UMA VEZ!\033[m')
            vitorias +=1
        else:
            print('\n\033[31mVOCE PERDEU! \033[m ')
            cpu +=1
            break

print(f'\n\033[31mGAME OVER! VOCE TEVE {vitorias} VITORIAS E EU {cpu}!\033[m')
