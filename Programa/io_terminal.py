from tabulate import tabulate



def imprime_lista(cabecalho, lista):
    #Prints a list of dictionaries formatted in a table.

    #:param header: Table header text.
   # :param list: List of dictionaries to be printed.
    
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
    #Pauses execution and waits for user input (press Enter)."""
    input("Pressione ENTER para continuar...")

def pergunta_id(questao, lista, mostra_lista=False):
    #Asks the user for an ID based on a list.

    #:param question: Text of the question.
    #:param list: List of items to choose from.
    #:param show_list: If True, show the list before asking for the ID.
    #:return: ID chosen by the user.
    
    if mostra_lista:
        imprime_lista(cabecalho="", lista=lista)

    while True:
        id = int(input(questao))
        if 0 <= id < len(lista):
            return id
        else:
            print(f"id inexistente. Tente de novo. Valores admitidos {0} - {len(lista)}")

