'''
ANSI escape sequence -  

\033[STYLE;TEXT;BACKGROUND m
\033[0;33;44m

STYLE: 0 (NONE), 1 (BOLD), 4(UNDERLINE), 7 (NEGATIVE)
TEXT: 30 (WHITE), 31(RED),32(GREEN),33(YELLOW),34(BLUE),35(PURPLE),36(CYAN),37(GREY)
BACK: 40 (WHITE), 41(RED),42(GREEN),43(YELLOW),44(BLUE),45(PURPLE)46(CYAN),47(GREY)
'''
cores = {'limpa':'\033[m', 
         'invertido':'\033[7;30m', 
         'branco':'\033[30m', 
         'vermelho':'\033[31m', 
         'verde':'\033[32m', 
         'amarelo':'\033[33m', 
         'azul':'\033[34m', 
         'magenta':'\033[35m', 
         'ciano':'\033[36m', 
         'cinza':'\033[37m'
         }

nome = input('Qual e o seu nome? :')
print('\nOla \033[1;34m{}\033[m, prazer em te conhecer!' .format(nome))
print('Ola {}{}{}, prazer em te conhecer!' .format('\033[1;35m', nome, '\033[m'))

print('Ola {}{}{}, prazer em te conhecer!' .format(cores['amarelo'], nome, cores['limpa']))

