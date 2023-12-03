from clientes import cria_novo_cliente, imprime_lista_de_clientes
from faturas import cria_nova_fatura, imprime_lista_de_faturas
from io_ficheiros import (carrega_as_listas_dos_ficheiros,
                          guarda_as_listas_em_ficheiros)
from io_terminal import pause
from veiculos import cria_novo_veiculo

def menu():
    """
    Menu principal da aplicação.

    Este menu oferece diversas opções para interagir com a aplicação de uma oficina mecânica fictícia.
    Os usuários podem cadastrar novos clientes, veículos, faturas, além de visualizar listagens e salvar/carregar dados.
    """

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
            # Função para guardar as listas de veículos, clientes e faturas nos arquivos
            guarda_as_listas_em_ficheiros(lista_de_veiculos, lista_de_clientes, lista_de_faturas)

        elif op == "c":
            # Função para carregar as listas de veículos, clientes e faturas dos arquivos
            lista_de_veiculos, lista_de_clientes, lista_de_faturas = carrega_as_listas_dos_ficheiros()

        elif op == "nc":
            # Função para criar um novo cliente e adicioná-lo à lista de clientes
            novo_cliente = cria_novo_cliente()
            if novo_cliente is not None:
                lista_de_clientes.append(novo_cliente)

        elif op == "nv":
            # Função para criar um novo veículo e adicioná-lo à lista de veículos
            novo_veiculo = cria_novo_veiculo()
            if novo_veiculo is not None:
                lista_de_veiculos.append(novo_veiculo)

        elif op == "nf":
            if len(lista_de_clientes) == 0 or len(lista_de_veiculos) == 0:
                print("Não há clientes ou veículos registrados...")
                continue

            # Função para criar uma nova fatura e adicioná-la à lista de faturas
            nova_fatura = cria_nova_fatura(lista_de_clientes, lista_de_veiculos)
            lista_de_faturas.append(nova_fatura)

        elif op == "lc":
            # Função para imprimir a lista de clientes
            imprime_lista_de_clientes(lista_de_clientes)
            # Função para pausar a execução e aguardar a entrada do usuário
            pause()

        elif op == "lv":
            # Função para imprimir a lista de veículos
            imprime_lista_de_veiculos(lista_de_veiculos)
            # Função para pausar a execução e aguardar a entrada do usuário
            pause()

        elif op == "lf":
            # Função para imprimir a lista de faturas
            imprime_lista_de_faturas(lista_de_faturas)
            # Função para pausar a execução e aguardar a entrada do usuário
            pause()

if __name__ == "__main__":
    menu()
