media_idade = 0
idad_hmvel = 0
quat_f_md20 = 0
soma_idade = 0
quant_f = 0
quant_m = 0

pessoas = int(input("Quantas pessoas você gostaria de analisar? "))
print("=-" * 20)

for c in range(1, pessoas + 1):
    nome = str(input(f"Digite o nome da {c}° pessoa: "))
    idade = int(input(f"Digite a idade da {c}° pessoa: "))
    sexo = str(input(f"Qual o sexo? Feminino(f)/ Masculino(m): "))
    print("=-" * 20)
    
    if sexo == "f":
        quant_f += 1
    elif sexo == "m":
        quat_m += 1
    
    soma_idade += idade
    media_idade = soma_idade / c
    
    if sexo == "m":
        if idade > idad_hmvel:
            idad_m_mvel = idade
            nom_m_mvel = nome
    
    if sexo == "f":
        if idade < 20:
            quat_f_md20 += 1

print(f"Media das idades é {media_idade}")

if quant_m > 0:
    print(f"O homem mais velho se chama {nom_m_mvel}")
else:
    print(f"Não apresenta homens")

if quant_f > 0:
    print(f"A quantidade de mulheres com menos de 20 anos são {quat_f_md20}")
else:
    print(f"Não apresenta mulheres")
