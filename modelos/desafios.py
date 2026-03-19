from json.decoder import NaN


class Musica:
    def __init__(self, nome, artista, duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

carro_bmw = Carro("BMW", "Preto", 2069)

class Restaurante:
    def __init__(self, nome, categoria, ano_criacao, nota):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.ano_criacao = int(ano_criacao)
        self.nota = int(nota)
    def __str__(self):
        return f'{self.nome} {self.categoria}'

restaurante_mexicano = Restaurante("Cacto", "Comida mexicana", 2069, 8)

print(restaurante_mexicano)

class Cliente:
    def __init__(self, nome, idade, genero, tamanho_peniano_em_cm):
        self.nome = nome
        self.idade = int(idade)
        self.genero = genero
        self.tamanho_peniano_em_cm = tamanho_peniano_em_cm

cliente_roberto = Cliente("Roberto", 67, "Masculino", 27)
cliente_ana = Cliente("Ana", 20, "Feminino", None)
cliente_valdemar = Cliente("Valdemar", 19, "Masculino", 6)



