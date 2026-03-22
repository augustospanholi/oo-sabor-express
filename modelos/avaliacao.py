class Avaliacao:
    def __init__(self, cliente, nota):
        self._cliente = cliente
        if nota > 5 or nota < 1:
            raise ValueError("A nota tem que estar entre 1 e 5")
        self._nota = nota

