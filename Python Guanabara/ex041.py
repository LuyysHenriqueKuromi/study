from datetime import date

ano_atual = date.today().year
ano_nasc = int(input('Em que ano você nasceu? '))
idade = ano_atual - ano_nasc
print('Você tem {} anos'.format(idade))

if idade <= 9:
    print('Sua categoria é MIRIM')
elif 9 < idade < 15:
    print('Sua categoria é INFANTIL')
elif 15 < idade < 20:
    print('Sua categoria é JUNIOR')
elif idade == 20:
    print('Sua categoria é SÊNIOR')
elif idade > 20:
    print('Sua categoria é MASTER')
