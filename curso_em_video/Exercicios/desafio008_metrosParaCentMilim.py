# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

print('='*5, 'Conversor de Metros para Centimetros e Milimetros', '='*5)
valor = float(input('\nDigite uma medida ou distancia em metros: '))

#cm = valor * 100
#mm = valor * 1000

#print('{}m, equivale a {:.0f}cm ou {:.0f}mm ' .format(valor, cm, mm))

# Usando o principio de economia de memoria e adicao de novas conversoes
print('A  mediada de {}m corresponde a: \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm' .format(valor, (valor/1000), (valor/100), (valor/10), (valor*10), (valor*100), (valor*1000)))