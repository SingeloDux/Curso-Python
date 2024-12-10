# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h,mostre uma mensagem dizendo que ele foi multado. A multa vai custar 20mt por cada km acima do limite.

speed = float(input('Qual era a velocidade do carro antes de ser parado? :'))

if speed > 80:   
    multa = (speed - 80) * 20
    print('\nVoce excedeu {:.0f}Km/h acima do limite permitida que e de 80Km/h. \n\033[31mVoce foi multado num valor de \033[4m{:.2f}MT\033[m!' .format(speed-80, multa))
else:
    print('\n\033[32mTenha um bom dia e dirija com seguranca!\033[m')