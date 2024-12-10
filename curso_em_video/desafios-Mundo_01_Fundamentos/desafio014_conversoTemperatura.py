# Escreva um programa que converta uma temperatura digitada em C e converta para F.

celsius = float(input('Informe a temperatura em celsius: '))
# fah = ((9 * celsius) / 5) + 32
fah = 9 * celsius / 5 + 32

print("A temperatura de {} Celsius corresponde a {} Fahreinheit! " .format(celsius, fah))