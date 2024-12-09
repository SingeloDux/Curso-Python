# Faca um programa que leia um numero inteiro e mostre na tela o seu sucessor e antecessor.

num = int(input('Digite um numero para saber seu antecessor e sucessor: '))

# antecessor = num -1
# sucessor = num + 1
# print('O numero digitado foi {}, seu antecessor e {} e o seu sucessor e {}!' .format(num, antecessor, sucessor))

# Nota: De modo a economizar memoria do dispositivo, a melhor opcao e a que nao faz uso de variaveis. Por tanto, e recomendado usar variaveis se elas forem necessarias para uso posterior, que nao e o caso do nosso codigo!

print('O numero digitado foi {}, seu antecessor e {} e o seu sucessor e {}!' .format(num, (num-1), (num+1)))

