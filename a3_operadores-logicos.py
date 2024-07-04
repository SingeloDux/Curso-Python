# True or False
# Comparadores: > >= == != <= < and or not

print('========================= PORTAL NERD =========================')
print('\t 1 - Univero DC Comics \n\t 2 - Universo Marvel \n\t 3 - Universo MillarWorld \n\t 0 - Outro Universo')
print('--------------------------------------------------------------')

opcao = input('Escolha um universo para ser teleportado ate la. Digite o nr: ')
print('--------------------------------------------------------------')

if opcao == '1':
    print('Bem vindo a DC Comics, aguarde um momento enquanto preparamos o seu tour pelas nossas instalacoes.')
elif opcao == '2':
    print('Bem vindo ao Universo Marvel, o seu tour pela torre dos vingadores iniciara em breve.')
elif opcao == '3':
    print('Bem vindo a Millar World, prepare-se para ter a sua bunda chutada pelo Kingsman.')
elif opcao == '0':
    print('Erro, teleporte indisponivel para outros universos')
else:
    print('Erro: Universo Inexistente')
print('--------------------------------------------------------------')
