#define os metodos q o repositorio precisa
from abc import ABC, abstractmethod

class PokemonInterface(ABC):

    @abstractmethod
    def cadastrar(self, pokemon):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def buscar(self, nome):
        pass

    @abstractmethod
    def editar(self, pokemon):
        pass

    @abstractmethod
    def excluir(self, id):
        pass