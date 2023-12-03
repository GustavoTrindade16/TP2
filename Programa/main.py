from clientes import cria_novo_cliente, imprime_lista_de_clientes
from faturas import cria_nova_fatura, imprime_lista_de_faturas
from io_ficheiros import (carrega_as_listas_dos_ficheiros,
                          guarda_as_listas_em_ficheiros)
from io_terminal import pause
from veiculos import cria_novo_veiculo

def menu():
   
   # Application main menu.

   # This menu offers several options for interacting with the application of a fictional mechanic shop.
   # Users can register new customers, vehicles, invoices, as well as view listings and save/upload data.
    

    lista_de_veiculos = []
    lista_de_clientes = []
    lista_de_faturas = []

    while True:
        print("""
        *********************************************************************
        :    (-: OFICINA BARATINHA - RESISTIMOS A QUALQUER ORÇAMENTO :-)    :
        *********************************************************************
        :                                                                   :
        : nc - novo cliente         lc - listagem de clientes               :
        : nv - novo veiculo         lv - listagem de veiculos               :
        : nf - nova fatura          lf - listagem das faturas               :
        : ...                                                               :
        : g - guarda tudo           c - carrega tudo                        :
        : x - sair                                                          :
        :                                                                   :
        *********************************************************************
        """)

        op = input("opcao?").lower()

        if op == "x":
            exit()

        elif op == "g":
            # Function to save lists of vehicles, customers and invoices in files
            guarda_as_listas_em_ficheiros(lista_de_veiculos, lista_de_clientes, lista_de_faturas)

        elif op == "c":
            # Function to load lists of vehicles, customers and invoices from files
            lista_de_veiculos, lista_de_clientes, lista_de_faturas = carrega_as_listas_dos_ficheiros()

        elif op == "nc":
            # Function to create a new customer and add it to the customer list
            novo_cliente = cria_novo_cliente()
            if novo_cliente is not None:
                lista_de_clientes.append(novo_cliente)

        elif op == "nv":
            # Function to create a new vehicle and add it to the vehicle list
            novo_veiculo = cria_novo_veiculo()
            if novo_veiculo is not None:
                lista_de_veiculos.append(novo_veiculo)

        elif op == "nf":
            if len(lista_de_clientes) == 0 or len(lista_de_veiculos) == 0:
                print("Não há clientes ou veículos registrados...")
                continue

            # Function to create a new invoice and add it to the invoice list
            nova_fatura = cria_nova_fatura(lista_de_clientes, lista_de_veiculos)
            lista_de_faturas.append(nova_fatura)

        elif op == "lc":
            # Function to print the customer list
            imprime_lista_de_clientes(lista_de_clientes)
            # Function to pause execution and wait for user input
            pause()

        elif op == "lv":
            # Function to pause execution and wait for user input
            imprime_lista_de_veiculos(lista_de_veiculos)
            # Function to pause execution and wait for user input
            pause()

        elif op == "lf":
            # Function to print the invoice list
            imprime_lista_de_faturas(lista_de_faturas)
            # Function to pause execution and wait for user input
            pause()

if __name__ == "__main__":
    menu()
