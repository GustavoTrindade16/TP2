from datetime import date
from io_terminal import imprime_lista, pergunta_id

nome_ficheiro_lista_de_faturas = "lista_de_faturas.pk"



def cria_nova_fatura(lista_de_clientes, lista_de_veiculos):
    """Cria uma nova fatura solicitando os dados ao usuário.

    Esta função interage com o usuário para obter informações sobre uma nova fatura,
    como o ID do cliente, o ID do veículo e a data da fatura. Retorna um dicionário
    contendo esses dados.

    :param lista_de_clientes: Lista de clientes disponíveis para seleção.
    :param lista_de_veiculos: Lista de veículos disponíveis para seleção.
    :return: Dicionário com os dados da nova fatura.
             Exemplo: {"cliente": <<id_cliente>>, "veiculo": <<id_veiculo>>, "data": <<data>>, ...}
    """
    

    id_cliente = pergunta_id(questao="Qual o id do cliente?", lista=lista_de_clientes, mostra_lista=True)
    id_veiculo = pergunta_id(questao="Qual o id do veículo?", lista=lista_de_veiculos, mostra_lista=True)

    nova_fatura = {"cliente": id_cliente,
                   "veiculo": id_veiculo,
                   "data": date.today()}

    return nova_fatura

def imprime_lista_de_faturas(lista_de_faturas):
    """Imprime a lista de faturas formatadamente.

    Esta função recebe uma lista de faturas e imprime seus dados de maneira formatada
    no terminal.

    :param lista_de_faturas: Lista de faturas a ser impressa.
                            Cada fatura é representada como um dicionário.
                            Exemplo: [{"cliente": <<id_cliente>>, "veiculo": <<id_veiculo>>, "data": <<data>>, ...}, {...}, ...]
    """
    # TODO: Implementar esta função
    # ...

# Exemplo de uso:
# lista_de_faturas = [...]  # Substitua isso com sua própria lista de faturas
# imprime_lista_de_faturas(lista_de_faturas)
