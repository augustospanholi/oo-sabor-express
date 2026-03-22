from modelos.restaurante import Restaurante

restaurante_games = Restaurante("Games", "Hamburgueria")

restaurante_games.receber_avaliacao("Enzo", 5)
restaurante_games.receber_avaliacao("ET", 4)
restaurante_games.receber_avaliacao("Pedro", 5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()