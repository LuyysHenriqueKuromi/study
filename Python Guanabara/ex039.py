from datetime import date

ano_atual = date.today().year
ano_nasc = int(input('Digite o ano e que você nasceu: '))
idade = ano_atual - ano_nasc

print(f'Quem nasceu em {ano_nasc} tem {idade} anos em {ano_atual}')

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    falta = 18 - idade
    print(f'Você ainda não tem 18 anos. Ainda faltam {falta} anos para o alistamento.')
    ano_ali = ano_atual + falta
    print(f'Seu alistamento será em {ano_ali}')
elif idade > 18:
    falta = idade - 18
    print(f'Você já deveria ter se alistado há {falta} anos.')
    ano_ali = ano_atual - falta
    print(f'Seu alistamento foi em {ano_ali}')
