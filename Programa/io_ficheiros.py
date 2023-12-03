import pickle
from clientes import nome_ficheiro_lista_de_clientes
from faturas import nome_ficheiro_lista_de_faturas
from veiculos import nome_ficheiro_lista_de_veiculos


def carrega_as_listas_dos_ficheiros():
    """Carrega as listas de veículos, clientes e faturas dos arquivos.

    Lê os dados dos arquivos correspondentes e retorna as listas.

    :return: Tupla contendo as listas de veículos, clientes e faturas.
    """
    lista_de_veiculos = le_de_ficheiro(nome_ficheiro_lista_de_veiculos)
    lista_de_clientes = le_de_ficheiro(nome_ficheiro_lista_de_clientes)
    lista_de_faturas = le_de_ficheiro(nome_ficheiro_lista_de_faturas)

    return lista_de_veiculos, lista_de_clientes, lista_de_faturas

def guarda_as_listas_em_ficheiros(lista_de_veiculos, lista_de_clientes, lista_de_faturas):
    """Guarda as listas de veículos, clientes e faturas nos arquivos.

    Pergunta ao usuário se deseja sobrescrever os dados existentes nos arquivos
    e, em caso afirmativo, salva as listas nos respectivos arquivos.

    :param lista_de_veiculos: Lista de veículos a ser salva.
    :param lista_de_clientes: Lista de clientes a ser salva.
    :param lista_de_faturas: Lista de faturas a ser salva.
    """
    op = input("Os dados nos ficheiros serão sobrepostos. Continuar (s/N)?")
    if op in ['s', 'S']:
        guarda_em_ficheiro(nome_ficheiro_lista_de_veiculos, lista_de_veiculos)
        guarda_em_ficheiro(nome_ficheiro_lista_de_clientes, lista_de_clientes)
        guarda_em_ficheiro(nome_ficheiro_lista_de_faturas, lista_de_faturas)
    else:
        print("Gravação cancelada...")

def guarda_em_ficheiro(nome_do_ficheiro, dados):
    """Guarda dados em um arquivo usando a biblioteca pickle.

    :param nome_do_ficheiro: Nome do arquivo.
    :param dados: Dados a serem salvos no arquivo.
    """
    with open(nome_do_ficheiro, "wb") as f:
        pickle.dump(dados, f)

def le_de_ficheiro(nome_ficheiro):
    """Lê dados de um arquivo usando a biblioteca pickle.

    :param nome_ficheiro: Nome do arquivo.
    :return: Dados lidos do arquivo.
    """
    with open(nome_ficheiro, "rb") as f:
        return pickle.load(f)
