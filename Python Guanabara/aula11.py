print('\033[31;43mOlá, mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[32m{} \033[me \033[31m{}\033[m!!!'.format(a, b))

nome = 'Luis'
cores = {'limpa':'\003[m', 
         'azul':'\033[34m', 
         'amarelo':'\033[33m', 
         'preto e branco':'\033[7;30m'}

print('Olá! Muito prezer em te conhecer, {}{}{}!!!'.format(cores['limpa'], nome, cores['limpa']))

'''\033[style; text; back m

text                 background

30      black        preto      40
31      red          vermelho   41
32      green        verde      42
33      yellow       amarelo    43
34      blue         azul       44
35      Magenta      Magenta    45
36      cyan         ciano      46
37      grey         cinza      47
97      white        branco     107

Exemplos
print('\033[0;30;41mOlá, Mundo\033[m')'''