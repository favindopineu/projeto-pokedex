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

```
pokedextk/
├── principal.py                
├── testar_repositorio.py       
├── config/
│   ├── BD.py                   
│   └── pokedex.db              
├── models/
│   └── pokemon.py              
├── interfaces/
│   └── pokemon_interface.py    
├── repositorio/
│   └── pokerepositorio.py       
└── controles/
    └── pokecontrole.py          
```

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

## 🚀 Como executar

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

Feito por **Carlos Eduardo Dias Sana** — [GitHub](https://github.com/favindopineu)

