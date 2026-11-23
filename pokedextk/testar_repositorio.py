#testa as funcionalidades
from models.pokemon import Pokemon
from repositorio.pokerepositorio import PokeRepositorio
from controles.pokecontrole import PokeControle


repositorio = PokeRepositorio()

pokemon = Pokemon(
    25,
    "Pikachu_Teste_123",
    "Elétrico",
    None,
    0.4,
    6.0,
    "Pokemon utilizado para testar o sistema"
)

id_teste = None

try:
    # TESTE 1 - CADASTRAR
    repositorio.cadastrar(pokemon)
    print("1. Pokémon cadastrado com sucesso!")

    # TESTE 2 - BUSCAR
    resultado = repositorio.buscar("Pikachu_Teste_123")

    if resultado:
        id_teste = resultado[0][0]
        pokemon.id = id_teste
        print("2. Pokémon encontrado com sucesso!")

        # TESTE 3 - EDITAR
        pokemon.nome = "Pikachu_Teste_Editado"
        repositorio.editar(pokemon)
        print("3. Pokémon editado com sucesso!")

        # TESTE 4 - LISTAR
        lista = repositorio.listar()
        print("4. Listagem realizada com sucesso!")
        print("Total de Pokémon no banco:", len(lista))

        # TESTE 5 - EXCLUIR
        repositorio.excluir(id_teste)
        id_teste = None
        print("5. Pokémon excluído com sucesso!")

    else:
        print("Não foi possível encontrar o Pokémon.")

finally:
    if id_teste is not None:
        repositorio.excluir(id_teste)


# TESTE 6 - CONTROLE
controle = PokeControle()

print("\n6. Controle conectado ao repositório com sucesso!")

print("\nTESTES FINALIZADOS!")