# Crie um programa que leia um numero e mostre o seu dobro, tripo e raiz quadrada.

num = int(input('Digite um numero para saber o seu dobro, triplo e raiz quadrada: '))

#dobro = num*2
#triplo = num*3
#raizQuad = num ** (1/2) #Ou pow(num, (1/2))

#print('O numero digitado foi {}, e o prometido foi: \nDobro: {} \nTriplo: {} \nRaiz Quadrada: {:.2f}' .format(num, dobro, triplo, raizQuad))

# Nota: De modo a economizar memoria do dispositivo, a melhor opcao e a que nao faz uso de variaveis. Por tanto, e recomendado usar variaveis se elas forem necessarias para uso posterior, que nao e o caso do nosso codigo!

print('O numero digitado foi {}, e o prometido foi: \nDobro: {} \nTriplo: {} \nRaiz Quadrada: {:.2f}' .format(num, (num*2), (num*3), (num ** (1/2))))