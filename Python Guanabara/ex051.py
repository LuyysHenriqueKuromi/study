prim_ter = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
quant = int(input('Digite a quantidade de termos: '))
termos = prim_ter

print(f'''O 1° termo da PA é {prim_ter} 
Sua razão é {razao}''')

for c in range(2, quant + 1):
    termos += razao
    print(f'O {c}° termo é {termos}')
