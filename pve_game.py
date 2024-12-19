from time import sleep
from random import randint

print('\n{:=^45}' .format('\033[1;34m PLAYER VERSUS ENVIROMENT \033[m'))

print('\nESCOLHA O JOGO QUE PRETENDE JOGAR!')
sleep(0.5)
print('[1] - JO KEN PO!') 
sleep(0.5)
print('[2] - ADVINHA O NUMERO!')
sleep(0.5)
print('[3] - PAR OU IMPAR!')
print('[0] - SAIR!')
opcao = int(input('Qual vai jogar?: '))

if opcao == 1:
    nomeJogo = ' PEDRA , PAPEL, TESOURA '
    print(f'\033[1;34m{nomeJogo:=^50}\033[m')
    print('FACA SUA ESCOLHA \n[1] - PEDRA ✊ \n[2] - PAPEL ✋\n[3] - TESOURA 🤞')

    itens = ('PEDRA', 'PAPEL', 'TESOURA')
    computador = randint(0,2)
    jogador = int(input('Qual e a sua jogada? : '))

    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')

    print('-='*30)
    print(f'Computador jogou {itens[computador]}')
    print(f'Voce jogou {itens[jogador]}')
    print('-='*30)

    if computador == 0: # PEDRA
        if jogador == 0:
            print('EMPATE!')
        elif jogador == 1:
            print('JOGADOR VENCEU!')
        elif jogador == 2:
            print('COMPUTADOR VENCEU!')
        else:
            print('JOGADA INVALIDA!')
    elif computador == 1: # PAPEL
        if jogador == 0:
            print('COMPUTADOR VENCEU!')
        elif jogador == 1:
            print('EMPATE')
        elif jogador == 2:
            print('JOGADOR VENCEU!')
        else:
            print('JOGADA INVALIDA!')
    elif computador == 2: #TESOURA
        if jogador == 0:
            print('JOGADOR VENCEU!')
        elif jogador == 1:
            print('COMPUTADOR VENCEU!')
        elif jogador == 2:
            print('EMPATE!')
        else:
            print('JOGADA INVALIDA!')
elif opcao == 2:
    nomeJogo = ' ADVINHE O NUMERO 🎲 '
    print(f'\n\033[1;33m{nomeJogo:=^60}\033[m')

    print('-='*30)
    print('\033[32mAcabei de pensar em um numero entre 0 e 10.\033[m')
    print('-='*30)
    computador = randint(0,10)
    jogador = int(input('Qual numero acabei de pensar? : '))
    palpites = 1
    while jogador != computador:
        if computador > jogador:   
            jogador = int(input('\nPalpite Errado! Tente um numero MAIOR: '))
            palpites +=1
        else:
            jogador = int(input('\nPalpite Errado! Tente um numero MENOR: '))
            palpites +=1
    if palpites > 1:
        print(f'\n\033[32mParabens! Depois de {palpites} palpites, voce finalmente acertou!\033[m')
    else:
        print(f'\n\033[32mParabens! Voce acertou com apenas {palpites} palpite!\033[m')
elif opcao == 3:

    separador = '-=-'*17
    nomeJogo = ' PAR🤜 OU 🤛IMPAR: O JOGO  '
    print(f'\n\033[1;32m{separador:^50}\n{nomeJogo:-^50}\n{separador:^50}\033[m')
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
elif opcao == 0:
    print('Obrigado por jogar! Volte mais vezes!')
else:
    print('Opcao invalida! Encerrando!')
