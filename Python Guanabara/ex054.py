from datetime import date

ano_atual = date.today().year

maioridade = 0
juventude = 0

for c in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {c}° pessoa: '))
    if ano_atual - ano >= 21:
        maioridade += 1
    else:
        juventude += 1

print(f'A quantidade de pessoas que atingiram a maioridade é {maioridade} e as que ainda não são {juventude}')
