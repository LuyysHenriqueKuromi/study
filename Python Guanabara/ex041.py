from datetime import date

ano_atual = date.today().year
ano_nasc = int(input('Em que ano você nasceu? '))
idade = ano_atual - ano_nasc
print(f'Você tem {idade} anos')

print('Sua classificação é', end=' ')
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
