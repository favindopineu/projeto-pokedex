# PokédexTK

Uma Pokédex de desktop feita em **Python** com interface gráfica em **Tkinter** e banco de dados **SQLite**. Permite cadastrar, consultar, editar e excluir Pokémon, e busca automaticamente a imagem de cada um na [PokéAPI](https://pokeapi.co/).

## Funcionalidades

- **Cadastrar** Pokémon com número da Pokédex, nome, tipos, altura e peso
- **Imagem automática**: o sprite do Pokémon é baixado da PokéAPI a partir do número informado e salvo no banco
- **Consultar** todos os Pokémon cadastrados em uma tabela
- **Visualizar a imagem** ao selecionar um Pokémon na tabela (redimensionada automaticamente conforme o tamanho da janela)
- **Editar** e **excluir** registros (com confirmação antes de excluir)
- **Validação** de campos: nome e Tipo 1 obrigatórios, aceita vírgula ou ponto em altura/peso

## Tecnologias

- Python 3.12+
- [Tkinter](https://docs.python.org/3/library/tkinter.html) (interface gráfica, já incluso no Python)
- [SQLite](https://www.sqlite.org/) via módulo `sqlite3` (já incluso no Python)
- [Pillow](https://pypi.org/project/pillow/) (manipulação e exibição das imagens)
- [PokéAPI](https://pokeapi.co/) (origem dos sprites)

## Estrutura do projeto

## 📁 Estrutura do projeto

| Caminho | Descrição |
|---------|-----------|
| [`principal.py`](./principal.py) | Interface gráfica (Tkinter) e ponto de entrada do programa |
| [`testar_repositorio.py`](./testar_repositorio.py) | Script de teste do CRUD |
| [`config/BD.py`](./config/BD.py) | Conexão com o banco SQLite |
| [`config/pokedex.db`](./config/pokedex.db) | Banco de dados |
| [`models/pokemon.py`](./models/pokemon.py) | Classe `Pokemon` (entidade) |
| [`interfaces/pokemon_interface.py`](./interfaces/pokemon_interface.py) | Interface abstrata com os métodos exigidos do repositório |
| [`repositorio/pokerepositorio.py`](./repositorio/pokerepositorio.py) | Operações no banco (cadastrar, listar, buscar, editar e excluir) |
| [`controles/pokecontrole.py`](./controles/pokecontrole.py) | Liga a interface gráfica ao repositório |

### Arquitetura

O projeto é dividido em camadas, cada uma com uma responsabilidade:

```
Interface gráfica (principal.py)
        ↓
Controle (PokeControle)
        ↓
Repositório (PokeRepositorio  ←  implementa PokemonInterface)
        ↓
Banco de dados SQLite (config/BD.py)
```

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/favindopineu/pokedextk.git
cd pokedextk
```

### 2. (Opcional) Crie um ambiente virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install pillow
```

> O Tkinter já vem com o Python no Windows e no macOS. No Linux (Debian/Ubuntu), instale com: `sudo apt install python3-tk`

### 4. Execute

```bash
python principal.py
```

> É necessário ter **conexão com a internet** para cadastrar Pokémon, pois a imagem é buscada na PokéAPI.

## Como usar

1. Na tela inicial, clique em **Cadastrar Pokémon**.
2. Preencha os dados (o número da Pokédex é usado para buscar a imagem) e clique em **Salvar Pokémon**.
3. Clique em **Consultar Pokémon** para ver a lista. Selecione um item para ver a imagem.
4. Use **Editar Pokémon** ou **Excluir Pokémon** com um item selecionado.

## Testes

O script `testar_repositorio.py` executa um teste simples do CRUD (cadastrar, buscar, editar, listar e excluir) usando um Pokémon temporário, que é removido ao final:

```bash
python testar_repositorio.py
```

## Autores

Feito por:
**Carlos Eduardoa** - [GitHub](https://github.com/favindopineu) <br>
**Erick Lavado** - [GitHub](https://github.com/Lavado-dev) <br>
**Lucas Barreto** - [GitHub](https://github.com/LucasB-Soares) <br>
**Felipe Xavier** - [GitHub](https://github.com/felipexsouza71) <br>
**Fabio Manfio** - [GitHub](https://github.com/Manfio19)




