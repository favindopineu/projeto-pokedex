#define a classe pokemon com seus atributos
class Pokemon:

    def __init__(
        self,
        numero,
        nome,
        tipo1,
        tipo2,
        altura,
        peso,
        descricao,
        imagem=None,
        id=None
    ):
        self.id = id
        self.numero = numero
        self.nome = nome
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.altura = altura
        self.peso = peso
        self.descricao = descricao
        self.imagem = imagem
