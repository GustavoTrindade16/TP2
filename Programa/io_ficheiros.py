import pickle
from clientes import nome_ficheiro_lista_de_clientes
from faturas import nome_ficheiro_lista_de_faturas
from veiculos import nome_ficheiro_lista_de_veiculos


def carrega_as_listas_dos_ficheiros():
    #Loads lists of vehicles, customers and invoices from files.

    #Reads data from corresponding files and returns lists.

   # :return: Tuple containing lists of vehicles, customers and invoices.
    
    lista_de_veiculos = le_de_ficheiro(nome_ficheiro_lista_de_veiculos)
    lista_de_clientes = le_de_ficheiro(nome_ficheiro_lista_de_clientes)
    lista_de_faturas = le_de_ficheiro(nome_ficheiro_lista_de_faturas)

    return lista_de_veiculos, lista_de_clientes, lista_de_faturas

def guarda_as_listas_em_ficheiros(lista_de_veiculos, lista_de_clientes, lista_de_faturas):
   #Save lists of vehicles, customers and invoices in files.

    #Asks the user if they want to overwrite existing data in the files
    #and, if so, saves the lists in the respective files.

   # :param vehicle_list: List of vehicles to be saved.
    #:param client_list: List of clients to be saved.
   # :param invoice_list: List of invoices to be saved.
    
    op = input("Os dados nos ficheiros serão sobrepostos. Continuar (s/N)?")
    if op in ['s', 'S']:
        guarda_em_ficheiro(nome_ficheiro_lista_de_veiculos, lista_de_veiculos)
        guarda_em_ficheiro(nome_ficheiro_lista_de_clientes, lista_de_clientes)
        guarda_em_ficheiro(nome_ficheiro_lista_de_faturas, lista_de_faturas)
    else:
        print("Gravação cancelada...")

def guarda_em_ficheiro(nome_do_ficheiro, dados):
   #Save data to a file using the pickle library.

    #:param file_name: Name of the file.
    #:param data: Data to be saved in the file.
    
    with open(nome_do_ficheiro, "wb") as f:
        pickle.dump(dados, f)

def le_de_ficheiro(nome_ficheiro):
    #Reads data from a file using the pickle library.

    #:param file_name: Name of the file.
    #:return: Data read from file.
    
    with open(nome_ficheiro, "rb") as f:
        return pickle.load(f)
