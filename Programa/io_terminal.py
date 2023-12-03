from tabulate import tabulate

# TODO: Copie para aqui o código de cada uma das funções nos
# ficheiros com o nome io_terminal*.py e faça um commit de cada vez
# Quando este ficheiro estiver completo com todas as suas funções,
# deve ser o único ficheiro io_terminal.py existente, deve apagar
# todos os outros ficheiros io_terminal-*.py, e inclusive estes comentários

# ...

def imprime_lista(cabecalho, lista):
    """Imprime uma lista de dicionários formatadamente em uma tabela.

    :param cabecalho: Texto do cabeçalho da tabela.
    :param lista: Lista de dicionários a ser impressa.
    """
    print(cabecalho)

    if len(lista) == 0:
        print("Lista vazia")
    else:
        # Cabeçalho da tabela
        lista_a_imprimir = [["id"] + list(lista[0].keys())]
        # Dados
        lista_a_imprimir.extend([[id] + list(d.values()) for id, d in enumerate(lista)])

        print(tabulate(lista_a_imprimir, headers="firstrow", tablefmt='psql'))

def pause():
    """Pausa a execução e espera pela entrada do usuário (pressionar Enter)."""
    input("Pressione ENTER para continuar...")

def pergunta_id(questao, lista, mostra_lista=False):
    """Pergunta ao usuário por um ID com base em uma lista.

    :param questao: Texto da pergunta.
    :param lista: Lista de itens para escolher.
    :param mostra_lista: Se True, mostra a lista antes de pedir o ID.
    :return: ID escolhido pelo usuário.
    """
    if mostra_lista:
        imprime_lista(cabecalho="", lista=lista)

    while True:
        id = int(input(questao))
        if 0 <= id < len(lista):
            return id
        else:
            print(f"id inexistente. Tente de novo. Valores admitidos {0} - {len(lista)}")

