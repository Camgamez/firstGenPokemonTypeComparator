import pickle
from requests_html import HTMLSession


class Pokemon:
    """
    Un pokemon tiene una propiedad número y una propiedad URL. Mas dos funciones para inicializarlas.
    """
    def __init__(self, number):
        self.__number = None
        self.__url = None
        self.setNumber(number)
        self.setURL(number)
    def setNumber(self, number):
        self.__number = number
    def getNumber(self):
        return self.__number
    def setURL(self, number):
        self.__url = "https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/movimientos_nivel&pk=" + number
    def getURL(self):
        return self.__url

    def getName(self):
        """Esta función abre una sesión de HTML y encuentra el nombre del pokemon."""
        session = HTMLSession()
        pokedexPage = session.get(self.getURL())

        name = pokedexPage.html.find("span", first=True).find(".mini", first=True).text

        return name
    def getImg(self):
        """
        Esta función consulta la dirección de la ubicación de la imagen del pokemon.
        """
        session = HTMLSession()
        pokedexPage = session.get(self.getURL())
        imgPokemon = pokedexPage.html.find(".pkmain", first=True).find(".center.bordedcho", first=True).find("img", first=True).attrs["src"]

        return imgPokemon

    """
    def getAllPokemon():
        try:
            # Buscamos el .pkl de pokemones
            with open("pokeDB.pkl", "rb") as pokeDB:
                allPokemon = pickle.load(pokeDB)
        except FileNotFoundError:
            # De no existir el .pkl de pokemones lo creamos
            allPokemon = []
            print("Creando .pkl")
            for number in range(151):
                allPokemon.append(getPokemon(number + 1))

            with open("pokeDB.pkl", "wb") as pokeDB:
                pickle.dump(allPokemon, pokeDB)

        return allPokemon
    """


