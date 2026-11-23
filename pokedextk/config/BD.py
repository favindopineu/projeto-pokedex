#faz conexao com o bd
import sqlite3
from pathlib import Path


class Database:

    @staticmethod
    def conectar():
        # Localiza o banco na mesma pasta deste arquivo (config/)
        caminho_banco = Path(__file__).resolve().parent / "pokedex.db"

        conexao = sqlite3.connect(caminho_banco)
        return conexao
