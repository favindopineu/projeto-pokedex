#cria interface grafica e a interacao com a pokedex
from urllib.request import urlopen, Request
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json

from PIL import Image, ImageTk, ImageOps
from io import BytesIO

from controles.pokecontrole import PokeControle

controle = PokeControle()


# BUSCAR IMAGEM NA POKEAPI
def buscar_imagem_pokemon(numero):
    endereco = f"https://pokeapi.co/api/v2/pokemon/{numero}"

    requisicao = Request(
        endereco,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    with urlopen(requisicao, timeout=10) as resposta:
        dados = json.loads(resposta.read().decode("utf-8"))

    imagem_url = dados["sprites"]["front_default"]

    if imagem_url is None:
        raise Exception("Imagem não encontrada para esse Pokémon!")

    requisicao_imagem = Request(
        imagem_url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    with urlopen(requisicao_imagem, timeout=10) as resposta_imagem:
        imagem = resposta_imagem.read()

    return imagem


# TELA DE CADASTRO
def abrir_cadastro():

    tela = tk.Toplevel(janela)
    tela.title("Cadastrar Pokémon")
    tela.geometry("450x600")

    titulo = tk.Label(
        tela,
        text="CADASTRAR POKÉMON",
        font=("Comic Sans MS", 20, "bold")
    )
    titulo.pack(pady=15)

    campos = {}

    nomes_campos = [
        "Número da Pokédex",
        "Nome",
        "Tipo 1",
        "Tipo 2",
        "Altura (m)",
        "Peso (kg)"
    ]

    for nome_campo in nomes_campos:

        label = tk.Label(
            tela,
            text=nome_campo,
            font=("Comic Sans MS", 11)
        )
        label.pack()

        entrada = tk.Entry(
            tela,
            font=("Comic Sans MS", 11),
            width=30
        )
        entrada.pack(pady=3)

        campos[nome_campo] = entrada

    # SALVAR POKÉMON
    def salvar_pokemon():

        try:
            numero = int(campos["Número da Pokédex"].get())
            nome = campos["Nome"].get().strip()
            tipo1 = campos["Tipo 1"].get().strip()
            tipo2 = campos["Tipo 2"].get().strip() or None

            altura = float(
                campos["Altura (m)"].get().replace(",", ".")
            )

            peso = float(
                campos["Peso (kg)"].get().replace(",", ".")
            )

            if not nome or not tipo1:
                messagebox.showwarning(
                    "Atenção",
                    "Preencha o nome e o Tipo 1!"
                )
                return

            # BUSCAR A IMAGEM
            imagem = buscar_imagem_pokemon(numero)

            # CADASTRAR NO BANCO
            controle.cadastrar(
                numero,
                nome,
                tipo1,
                tipo2,
                altura,
                peso,
                "",
                imagem
            )

            messagebox.showinfo(
                "Sucesso",
                "Pokémon cadastrado com sucesso!"
            )

            tela.destroy()

        except ValueError:
            messagebox.showerror(
                "Erro",
                "Confira os campos numéricos!"
            )

        except Exception as erro:
            messagebox.showerror(
                "Erro",
                f"Não foi possível cadastrar.\n{erro}"
            )

    tk.Button(
        tela,
        text="Salvar Pokémon",
        font=("Comic Sans MS", 13, "bold"),
        command=salvar_pokemon
    ).pack(pady=20)


# TELA DE CONSULTA
def abrir_consulta():

    tela = tk.Toplevel(janela)
    tela.title("Consultar Pokémon")
    tela.geometry("850x600")

    titulo = tk.Label(
        tela,
        text="POKÉMON CADASTRADOS",
        font=("Comic Sans MS", 20, "bold")
    )
    titulo.pack(pady=15)

    # QUADRO QUE CONTÉM A TABELA E A IMAGEM
    quadro_conteudo = tk.Frame(
        tela,
        bg="#eeeeee"
    )

    quadro_conteudo.pack(
        padx=10,
        pady=5,
        fill="both",
        expand=True
    )

    # TABELA
    tabela = ttk.Treeview(
        quadro_conteudo,
        columns=("ID", "Número", "Nome", "Tipo 1", "Tipo 2"),
        show="headings",
        height=10
    )

    tabela.heading("ID", text="ID")
    tabela.heading("Número", text="Número")
    tabela.heading("Nome", text="Nome")
    tabela.heading("Tipo 1", text="Tipo 1")
    tabela.heading("Tipo 2", text="Tipo 2")

    tabela.column("ID", width=40)
    tabela.column("Número", width=65)
    tabela.column("Nome", width=100)
    tabela.column("Tipo 1", width=75)
    tabela.column("Tipo 2", width=75)

    tabela.pack(
        side="left",
        fill="y",
        expand=False
    )

    # ESPAÇO RESERVADO PARA A IMAGEM
    quadro_imagem = tk.Frame(
        quadro_conteudo,
        width=350,
        height=350,
        bg="#eeeeee"
    )

    quadro_imagem.pack(
        side="right",
        padx=20,
        pady=10
    )

    # IMPEDE QUE A IMAGEM AUMENTE O QUADRO
    quadro_imagem.pack_propagate(False)

    label_imagem = tk.Label(
        quadro_imagem,
        text="Selecione um Pokémon",
        bg="#eeeeee",
        font=("Comic Sans MS", 11)
    )

    label_imagem.pack(
        fill="both",
        expand=True
    )

    # MOSTRAR IMAGEM AO SELECIONAR
    def mostrar_imagem(event):

        selecionado = tabela.selection()

        if not selecionado:
            return

        valores = tabela.item(
            selecionado[0],
            "values"
        )

        id_pokemon = int(valores[0])

        pokemons = controle.listar()

        for pokemon in pokemons:

            if pokemon[0] == id_pokemon:

                if pokemon[8] is None:
                    label_imagem.config(
                        image="",
                        text="Imagem não disponível"
                    )

                    label_imagem.image = None

                    if hasattr(label_imagem, "imagem_original"):
                        del label_imagem.imagem_original

                    return

                # CARREGAR IMAGEM ORIGINAL
                imagem_original = Image.open(
                    BytesIO(pokemon[8])
                )

                label_imagem.imagem_original = imagem_original

                # REDIMENSIONAR
                redimensionar_imagem()

                break

    # REDIMENSIONAR IMAGEM AUTOMATICAMENTE
    def redimensionar_imagem(event=None):

        if not hasattr(label_imagem, "imagem_original"):
            return

        largura = label_imagem.winfo_width()
        altura = label_imagem.winfo_height()

        if largura <= 1 or altura <= 1:
            return

        imagem = ImageOps.contain(
            label_imagem.imagem_original,
            (largura, altura),
            method=Image.Resampling.LANCZOS
        )

        foto = ImageTk.PhotoImage(imagem)

        label_imagem.config(
            image=foto,
            text=""
        )

        # MANTER REFERÊNCIA DA IMAGEM
        label_imagem.image = foto

    # ATUALIZAR IMAGEM QUANDO O ESPAÇO MUDAR
    label_imagem.bind(
        "<Configure>",
        redimensionar_imagem
    )

    # VINCULAR SELEÇÃO DA TABELA
    tabela.bind(
        "<<TreeviewSelect>>",
        mostrar_imagem
    )

    # CARREGAR POKÉMON DO BANCO
    try:
        pokemons = controle.listar()

        for pokemon in pokemons:

            tabela.insert(
                "",
                "end",
                values=(
                    pokemon[0],
                    pokemon[1],
                    pokemon[2],
                    pokemon[3],
                    pokemon[4] or "-"
                )
            )

    except Exception as erro:
        messagebox.showerror(
            "Erro",
            f"Não foi possível consultar.\n{erro}"
        )
        return

    # EXCLUIR POKÉMON
    def excluir_pokemon():

        selecionado = tabela.selection()

        if not selecionado:
            messagebox.showwarning(
                "Atenção",
                "Selecione um Pokémon para excluir!"
            )
            return

        confirmar = messagebox.askyesno(
            "Confirmar exclusão",
            "Deseja realmente excluir este Pokémon?"
        )

        if confirmar:

            valores = tabela.item(
                selecionado[0],
                "values"
            )

            id_pokemon = int(valores[0])

            try:
                controle.excluir(id_pokemon)

                tabela.delete(selecionado[0])

                # LIMPAR IMAGEM
                label_imagem.config(
                    image="",
                    text="Selecione um Pokémon"
                )

                label_imagem.image = None

                if hasattr(label_imagem, "imagem_original"):
                    del label_imagem.imagem_original

                messagebox.showinfo(
                    "Sucesso",
                    "Pokémon excluído com sucesso!"
                )

            except Exception as erro:
                messagebox.showerror(
                    "Erro",
                    f"Não foi possível excluir.\n{erro}"
                )

    # EDITAR POKÉMON
    def editar_pokemon():

        selecionado = tabela.selection()

        if not selecionado:
            messagebox.showwarning(
                "Atenção",
                "Selecione um Pokémon para editar!"
            )
            return

        valores = tabela.item(
            selecionado[0],
            "values"
        )

        id_pokemon = int(valores[0])

        try:
            todos_pokemons = controle.listar()

            pokemon = None

            for item in todos_pokemons:

                if item[0] == id_pokemon:
                    pokemon = item
                    break

            if pokemon is None:
                messagebox.showerror(
                    "Erro",
                    "Pokémon não encontrado!"
                )
                return

        except Exception as erro:
            messagebox.showerror(
                "Erro",
                f"Não foi possível carregar os dados.\n{erro}"
            )
            return

        tela_edicao = tk.Toplevel(tela)
        tela_edicao.title("Editar Pokémon")
        tela_edicao.geometry("450x600")

        titulo_edicao = tk.Label(
            tela_edicao,
            text="EDITAR POKÉMON",
            font=("Comic Sans MS", 20, "bold")
        )

        titulo_edicao.pack(pady=15)

        campos = {}

        nomes_campos = [
            "Número da Pokédex",
            "Nome",
            "Tipo 1",
            "Tipo 2",
            "Altura (m)",
            "Peso (kg)"
        ]

        dados = [
            pokemon[1],
            pokemon[2],
            pokemon[3],
            pokemon[4] or "",
            pokemon[5],
            pokemon[6]
        ]

        for nome_campo, dado in zip(nomes_campos, dados):

            label = tk.Label(
                tela_edicao,
                text=nome_campo,
                font=("Comic Sans MS", 11)
            )

            label.pack()

            entrada = tk.Entry(
                tela_edicao,
                font=("Comic Sans MS", 11),
                width=30
            )

            entrada.pack(pady=3)

            entrada.insert(0, str(dado))

            campos[nome_campo] = entrada

        # SALVAR EDIÇÃO
        def salvar_edicao():

            try:
                numero = int(
                    campos["Número da Pokédex"].get()
                )

                nome = campos["Nome"].get().strip()

                tipo1 = campos["Tipo 1"].get().strip()

                tipo2 = campos["Tipo 2"].get().strip() or None

                altura = float(
                    campos["Altura (m)"].get().replace(",", ".")
                )

                peso = float(
                    campos["Peso (kg)"].get().replace(",", ".")
                )

                if not nome or not tipo1:
                    messagebox.showwarning(
                        "Atenção",
                        "Preencha o nome e o Tipo 1!"
                    )
                    return

                controle.editar(
                    id_pokemon,
                    numero,
                    nome,
                    tipo1,
                    tipo2,
                    altura,
                    peso,
                    "",
                    pokemon[8]
                )

                tabela.item(
                    selecionado[0],
                    values=(
                        id_pokemon,
                        numero,
                        nome,
                        tipo1,
                        tipo2 or "-"
                    )
                )

                messagebox.showinfo(
                    "Sucesso",
                    "Pokémon editado com sucesso!"
                )

                tela_edicao.destroy()

            except ValueError:
                messagebox.showerror(
                    "Erro",
                    "Confira os campos numéricos!"
                )

            except Exception as erro:
                messagebox.showerror(
                    "Erro",
                    f"Não foi possível editar.\n{erro}"
                )

        tk.Button(
            tela_edicao,
            text="Salvar alterações",
            font=("Comic Sans MS", 13, "bold"),
            command=salvar_edicao
        ).pack(pady=20)

    # QUADRO DOS BOTÕES
    botoes = tk.Frame(tela)
    botoes.pack(pady=10)

    # BOTÃO EDITAR
    tk.Button(
        botoes,
        text="Editar Pokémon",
        font=("Comic Sans MS", 12, "bold"),
        command=editar_pokemon
    ).pack(side="left", padx=10)

    # BOTÃO EXCLUIR
    tk.Button(
        botoes,
        text="Excluir Pokémon",
        font=("Comic Sans MS", 12, "bold"),
        command=excluir_pokemon
    ).pack(side="left", padx=10)


# JANELA PRINCIPAL
janela = tk.Tk()

janela.title("Pokédex")
janela.geometry("800x600")

titulo = tk.Label(
    janela,
    text="POKÉDEX",
    font=("Comic Sans MS", 25, "bold")
)

titulo.pack(pady=30)

botao = tk.Button(
    janela,
    text="Cadastrar Pokémon",
    font=("Comic Sans MS", 14, "bold"),
    command=abrir_cadastro
)

botao.pack(pady=10)

botao2 = tk.Button(
    janela,
    text="Consultar Pokémon",
    font=("Comic Sans MS", 14, "bold"),
    command=abrir_consulta
)

botao2.pack(pady=10)

janela.mainloop()