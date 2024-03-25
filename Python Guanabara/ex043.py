peso = float(input('Digite o seu peso em Kg: '))
altura = float(input('Digite a sua altura em m: '))
imc = peso / (altura**2)
print(f'Seu IMC é de cerca de {imc:.1f}')

if imc < 18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('PESO IDEAL')
elif 25 <= imc < 30:
    print('SOBREPESO')
elif 30 <= imc < 40:
    print('OBESIDADE')
elif imc >= 40:
    print('OBESIDADE MÓRBIDA')
