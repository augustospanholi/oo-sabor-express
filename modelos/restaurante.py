class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'

    def listar_restaurantes():

        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | Status')

        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante._ativo}')

restaurante_madero = Restaurante("Madero", "Hamburgueria")
restaurante_yume = Restaurante("Yume", "Japonesa")
restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_pizza = Restaurante("Pizza Express", "Italiana")

Restaurante.listar_restaurantes()