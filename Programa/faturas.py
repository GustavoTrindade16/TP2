from datetime import date
from io_terminal import imprime_lista, pergunta_id

nome_ficheiro_lista_de_faturas = "lista_de_faturas.pk"



def cria_nova_fatura(lista_de_clientes, lista_de_veiculos):
        #Creates a new invoice requesting data from the user.

    #This function interacts with the user to obtain information about a new invoice,
    #such as customer ID, vehicle ID and invoice date. Returns a dictionary
    #containing this data.

    #:param client_list: List of clients available for selection.
    #:param vehicle_list: List of vehicles available for selection.
    #:return: Dictionary with the new invoice data.
    #Example: {"customer": <<client_id>>, "vehicle": <<vehicle_id>>, "data": <<date>>, ...}
    

    id_cliente = pergunta_id(questao="Qual o id do cliente?", lista=lista_de_clientes, mostra_lista=True)
    id_veiculo = pergunta_id(questao="Qual o id do veículo?", lista=lista_de_veiculos, mostra_lista=True)

    nova_fatura = {"cliente": id_cliente,
                   "veiculo": id_veiculo,
                   "data": date.today()}

    return nova_fatura

def imprime_lista_de_faturas(lista_de_faturas):
    #Prints the list of invoices formatted.

    #This function receives a list of invoices and prints their data in a formatted format.
    #at the terminal.

   # :param invoice_list: List of invoices to be printed.
        #                    Each invoice is represented as a dictionary.
                  #          Example: [{"customer": <<client_id>>, "vehicle": <<vehicle_id>>, "data": <<date>>, ...}, {...}, ...]
    
   

# Exemplo de uso:
# lista_de_faturas = [...]  # Substitua isso com sua própria lista de faturas
# imprime_lista_de_faturas(lista_de_faturas)
