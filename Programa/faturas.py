from datetime import date

from io_terminal import imprime_lista, pergunta_id

nome_ficheiro_lista_de_faturas = "lista_de_faturas.pk"


# TODO: Copie para aqui o código de cada uma das funções nos
# ficheiros com o nome faturas*.py e faça um commit de cada vez
# Quando este ficheiro estiver completo com todas as suas funções,
# deve ser o unico ficheiro faturas.py existente, deve apagar
# todos os outros ficheiros faturas-*.py, e inclusive estes comentários

# ...

def cria_nova_fatura(lista_de_clientes, lista_de_veiculos):
    """Pede ao utilizador para introduzir os dados de uma nova fatura

    :return: dicionario com uma fatura, na forma
        {"cliente": <<id_cliente>>, "veiculo": <<id_veiculo>>, "data": <<data>>, ...}
    """

    id_cliente = pergunta_id(questao="Qual o id do cliente?", lista=lista_de_clientes, mostra_lista=True)
    id_veiculo = pergunta_id(questao="Qual o id do veiculo?", lista=lista_de_veiculos, mostra_lista=True)

    # TODO: Pedir o resto dos dados da fatura, e não esquecer de os guardar no dicionario
    # ...

    fatura = {"cliente": id_cliente,
              "veiculo": id_veiculo,
              "data": date.today()}

    return fatura

def imprime_lista_de_faturas(lista_de_faturas):
    """TODO: documentação"""

    # TODO: Implementar esta função
    # ...
    pass
