class Cachorros:
    def __init__(self, nome, cor_de_pelo, idade, tamanho):
        self.nome = nome
        self.cor_de_pelo = cor_de_pelo
        self.idade = idade
        self.tamanho = tamanho
    def latir(self):
        print('au au')
    def corre(self):
        print(f'{self.nome} esta correndo')

cachorro_1 = Cachorros('Toby', 'marrom', 5, 'grande')

print(cachorro_1.nome)
cachorro_1.latir()
cachorro_1.corre()

cachorro_2 = Cachorros('Max', 'preto', 3, 'pequeno')
print(cachorro_2.tamanho)