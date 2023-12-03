from io_terminal import imprime_lista

nome_ficheiro_lista_de_veiculos = "lista_de_veiculos.pk"

def imprime_lista_de_veiculos(lista_de_veiculos):
    """Imprime a lista de veículos formatadamente.

    Esta função recebe uma lista de veículos e imprime seus dados de maneira formatada
    no terminal, utilizando a função `imprime_lista` do módulo `io_terminal`.

    :param lista_de_veiculos: Lista de veículos a ser impressa.
                              Cada veículo é representado como um dicionário.
                              Exemplo: [{"marca": "Toyota", "matricula": "AB123CD", ...}, {...}, ...]
    """
    imprime_lista(cabecalho="Lista de Veículos", lista=lista_de_veiculos)

def cria_novo_veiculo():
    """Pede ao utilizador para introduzir um novo veículo.

    :return: Dicionário com os dados do novo veículo.
             Exemplo: {"marca": "Toyota", "matricula": "AB123CD", ...}
    """
    marca = input("marca? ")
    matricula = input("matricula? ").upper()
    # TODO: Pedir o resto dos dados do veículo, e não esquecer de guardá-los no dicionário
    # ...

    veiculo = {"marca": marca,
               "matricula": matricula}

    return veiculo
