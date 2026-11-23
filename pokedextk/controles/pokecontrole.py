#faz ligacao entre interface grafica e o repositorio
from models.pokemon import Pokemon
from repositorio.pokerepositorio import PokeRepositorio


class PokeControle:

    def __init__(self):
        self.repositorio = PokeRepositorio()

    def cadastrar(self, numero, nome, tipo1, tipo2, altura, peso, descricao, imagem=None):
        pokemon = Pokemon(
            numero, nome, tipo1, tipo2,
            altura, peso, descricao, imagem
        )

        self.repositorio.cadastrar(pokemon)

    def listar(self):
        return self.repositorio.listar()

    def buscar(self, nome):
        return self.repositorio.buscar(nome)

    def editar(self, id, numero, nome, tipo1, tipo2, altura, peso, descricao, imagem=None):
        pokemon = Pokemon(
            numero, nome, tipo1, tipo2,
            altura, peso, descricao, imagem, id
        )

        self.repositorio.editar(pokemon)

    def excluir(self, id):
        self.repositorio.excluir(id)