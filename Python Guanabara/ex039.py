from datetime import date

ano_atual = date.today().year
ano_nasc = int(input('Digite o ano e que você nasceu: '))
idade = ano_atual - ano_nasc

print('Quem nasceu em {} tem {} em {}'.format(ano_nasc, idade, ano_atual))

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano_ali = ano_atual + saldo
    print('Seu alistamento será em {}'.format(ano_ali))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano_ali = ano_atual - saldo
    print('Seu alistamento foi em {}'.format(ano_ali))
