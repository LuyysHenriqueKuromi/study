carro = int(input('Qual a sua velocidade em Km/h? '))
if carro > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (carro - 80)*7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
