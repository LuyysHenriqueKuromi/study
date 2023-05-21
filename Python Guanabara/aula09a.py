frase = 'Curso em Vídeo Python'

#FATIAMENTO
print(frase[9:14])
#entre [] o indice da string, antes do dois pontos é onde vai começar : depois é onde vai parar
#excluindo o ultimo e considerando um a menos, Exp: 15, não conta o 15, mas conta o 14 como ultimo

#[9:21:2] ele vai começar do 9 até o 21 pulando de dois em dois = VdoPto
#[:5] ele vai começar no inicio e vai até 5 = Curso
#[15:] ele vai começar no 15 até o final = Python
#[9::3] ele vai começar no 9 até o final pulando de três em três = VePh

#ANÁLISE
print(len(frase))
#len é a quantidade de caracteres dentro da frase

print(frase.count('o'))
#count é contar quantas vezes ('...') o valor entre aspas apareceu

print(frase.find('deo'))
#find é onde ele encontrou ('...') o valor entre aspas = 11 se for mais de um caractere ele fala o primeiro valor 
#e a posição, -1 = não encontrou na string

print('Curso' in frase)
#vai falar se dentro da frase existe a pelavra 'Curso', True para sim, False para não

#TRANSFORMAÇÃO
print(frase.replace('Python','Android'))
#onde tiver 'Python' ele vai substituir por 'Android' = 'Curso em Vídeo Android'

print(frase.upper())
#pegar em minusculo e substituir por maiusculo = 'CURSO EM VÍDEO PYTHON'

print(frase.lower())
#pegar em maiusculo e substituir por minusculo = 'curso em vídeo python'

print(frase.capitalize())
#pegar todos os caracteres para minusculos e a primeira letra ele joga para maiuscula = 'Curso em vídeo python'

print(frase.title())
#é o capitalize palavra por palavra onde tiver espaços = 'Curso Em Vídeo Python'

print(frase.strip())
#remover os todos os espaços inuteis tanto da direita quanto da esquerda
#rstrip() só os espaços da direita, lstrip() apenas os da esquerda

#DIVISÃO
print(frase.split())
#vai fazer uma divisão dentro string considerando os espaços em uma lista
# Curso em Vídeo Python
# 01234 01 01234 012345
# -0-- --1-- --2-- --3-

dividido = frase.split()
print(dividido[0][3])
#ele vai mostra o valor [...] da lista, sendo 0 = Curso
#ele vai pegar o dividido 0 e mostrar o valor [...], sendo o dividido 0, casa 3 = s

#JUNÇÃO
print('-'.join(frase))
#vai juntar todos os elementos de frase e vai usar o sepador '-' = 'Curso-em-Vídeo-Python'