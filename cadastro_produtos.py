
import sqlite3


def conectar_banco():
    return sqlite3.connect("estoque.db")


def criar_tabela():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS estoque (
        codigo TEXT PRIMARY KEY,
        nome_item TEXT NOT NULL,
        quantidade REAL NOT NULL,
        unidade_medida TEXT NOT NULL,
        preco_unitario REAL NOT NULL,
        preco_total REAL NOT NULL
    )
    """)

    conexao.commit()
    conexao.close()


# CREATE
def cadastrar_produto():
    print("\n--- CADASTRO DE PRODUTO ---")

    codigo = input("Digite o código do produto (001 a 999): ")

    if not codigo.isdigit() or len(codigo) != 3:
        print("Erro: o código deve conter 3 números.")
        return

    nome_item = input("Digite o nome do item: ")
    quantidade = float(input("Digite a quantidade em estoque: "))
    unidade_medida = input("Digite a unidade de medida (un, kg, L, m): ")
    preco_unitario = float(input("Digite o preço unitário: "))

    preco_total = quantidade * preco_unitario

    conexao = conectar_banco()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        INSERT INTO estoque (
            codigo,
            nome_item,
            quantidade,
            unidade_medida,
            preco_unitario,
            preco_total
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            codigo,
            nome_item,
            quantidade,
            unidade_medida,
            preco_unitario,
            preco_total
        ))

        conexao.commit()

        print("\nProduto cadastrado com sucesso!")
        print(f"Preço total em estoque: R$ {preco_total:.2f}")

    except sqlite3.IntegrityError:
        print("\nErro: já existe um produto com esse código.")

    conexao.close()


# READ
def listar_produtos():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM estoque")
    produtos = cursor.fetchall()

    print("\n--- PRODUTOS CADASTRADOS ---")

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
    else:
        for produto in produtos:
            print(f"""
Código: {produto[0]}
Nome: {produto[1]}
Quantidade: {produto[2]}
Unidade: {produto[3]}
Preço unitário: R$ {produto[4]:.2f}
Preço total: R$ {produto[5]:.2f}
------------------------------
""")

    conexao.close()


# UPDATE
def atualizar_produto():
    print("\n--- ATUALIZAR PRODUTO ---")

    codigo = input("Digite o código do produto: ")

    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM estoque WHERE codigo = ?", (codigo,))
    produto = cursor.fetchone()

    if produto is None:
        print("Produto não encontrado.")

    else:
        nova_quantidade = float(input("Digite a nova quantidade: "))
        novo_preco = float(input("Digite o novo preço unitário: "))

        novo_preco_total = nova_quantidade * novo_preco

        cursor.execute("""
        UPDATE estoque
        SET quantidade = ?,
            preco_unitario = ?,
            preco_total = ?
        WHERE codigo = ?
        """, (
            nova_quantidade,
            novo_preco,
            novo_preco_total,
            codigo
        ))

        conexao.commit()

        print("Produto atualizado com sucesso!")

    conexao.close()


# DELETE
def remover_produto():
    print("\n--- REMOVER PRODUTO ---")

    codigo = input("Digite o código do produto: ")

    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM estoque WHERE codigo = ?", (codigo,))
    produto = cursor.fetchone()

    if produto is None:
        print("Produto não encontrado.")

    else:
        cursor.execute("""
        DELETE FROM estoque
        WHERE codigo = ?
        """, (codigo,))

        conexao.commit()

        print("Produto removido com sucesso!")

    conexao.close()


# MENU
def menu():

    criar_tabela()

    while True:

        print("""
===== SISTEMA DE ESTOQUE =====

1 - Cadastrar produto
2 - Listar produtos
3 - Atualizar produto
4 - Remover produto
5 - Sair

""")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()

        elif opcao == "2":
            listar_produtos()

        elif opcao == "3":
            atualizar_produto()

        elif opcao == "4":
            remover_produto()

        elif opcao == "5":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")


menu()
