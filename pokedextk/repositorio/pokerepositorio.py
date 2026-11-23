#executa as operacoes no banco de dados
from config.BD import Database
from interfaces.pokemon_interface import PokemonInterface


class PokeRepositorio(PokemonInterface):

    def cadastrar(self, pokemon):
        conexao = Database.conectar()
        cursor = conexao.cursor()

        try:
            sql = """
            INSERT INTO pokemon
            (numero, nome, tipo1, tipo2, altura, peso, descricao, imagem)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """

            valores = (
                pokemon.numero,
                pokemon.nome,
                pokemon.tipo1,
                pokemon.tipo2,
                pokemon.altura,
                pokemon.peso,
                pokemon.descricao,
                pokemon.imagem
            )

            cursor.execute(sql, valores)
            conexao.commit()

        finally:
            cursor.close()
            conexao.close()

    def listar(self):
        conexao = Database.conectar()
        cursor = conexao.cursor()

        try:
            cursor.execute("SELECT * FROM pokemon")
            resultado = cursor.fetchall()
            return resultado

        finally:
            cursor.close()
            conexao.close()

    def buscar(self, nome):
        conexao = Database.conectar()
        cursor = conexao.cursor()

        try:
            cursor.execute(
                "SELECT * FROM pokemon WHERE nome LIKE ?",
                (f"%{nome}%",)
            )

            resultado = cursor.fetchall()
            return resultado

        finally:
            cursor.close()
            conexao.close()

    def editar(self, pokemon):
        conexao = Database.conectar()
        cursor = conexao.cursor()

        try:
            sql = """
            UPDATE pokemon SET
            numero=?,
            nome=?,
            tipo1=?,
            tipo2=?,
            altura=?,
            peso=?,
            descricao=?,
            imagem=?
            WHERE id=?
            """

            valores = (
                pokemon.numero,
                pokemon.nome,
                pokemon.tipo1,
                pokemon.tipo2,
                pokemon.altura,
                pokemon.peso,
                pokemon.descricao,
                pokemon.imagem,
                pokemon.id
            )

            cursor.execute(sql, valores)
            conexao.commit()

        finally:
            cursor.close()
            conexao.close()

    def excluir(self, id):
        conexao = Database.conectar()
        cursor = conexao.cursor()

        try:
            cursor.execute(
                "DELETE FROM pokemon WHERE id=?",
                (id,)
            )

            conexao.commit()

        finally:
            cursor.close()
            conexao.close()