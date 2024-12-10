# Estrutura Sequencial: Todos os blocos do programa sao executados!
# Estrutura Condicional: Apenas o bloco "True" ou "False" sera executado, nunca os dois!
# Comparadores: > | >= | == | !=  | <=  | <  | and | or | not

nome = str(input('Por favor informe o seu nome para iniciar o Tour: '))

print('\n{:=^50}' .format(' PORTAL NERD '))

opcao = input('Ola {}, bem vindo ao portal nerd! Por favor selecione um universo para teleporte! \n1 - DC Comics |\t2 - Marvel |\t3 - MillarWorld |\t0 - Cancelar \n\nDigite o nr: ' .format(nome))

if opcao == '1':
    print('\n\033[34mBem vindo a \033[1mDC Comics\033[m\033[34m, aguarde um momento enquanto preparamos o seu tour pela Sala da Justica.\033[m')
elif opcao == '2':
    print('\n\033[31mBem vindo ao Universo Marvel, o seu tour pela torre dos vingadores iniciara em breve.')
elif opcao == '3':
    print('\n\033[33mBem vindo a Millar World, prepare-se para ter a sua bunda chutada pelo Kingsman.')
elif opcao == '0':
    print('\nCancelando o teleporte. Obigado pela visita!')
else:
    print('\nErro: Universo Inexistente')
