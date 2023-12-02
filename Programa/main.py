from clientes import cria_novo_cliente, imprime_lista_de_clientes
from faturas import cria_nova_fatura, imprime_lista_de_faturas
from io_ficheiros import (carrega_as_listas_dos_ficheiros,
                          guarda_as_listas_em_ficheiros)
from io_terminal import pause
from veiculos import cria_novo_veiculo, imprime_lista_de_veiculos



####################################################################
#
# TODO: Copie para aqui o código de cada uma das funções nos
# ficheiros com o nome main-*.py e faça um commit de cada vez
# Quando este ficheiro estiver completo com todas as suas funções,
# deve ser o unico ficheiro main.py existente, deve apagar
# todos os outros ficheiros main-*.py, e inclusive estes comentários

# ...

####################################################################

def menu():
    """Menu principal da aplicação"""

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
            guarda_as_listas_em_ficheiros(lista_de_veiculos, lista_de_clientes, lista_de_faturas)

        elif op == "c":
            lista_de_veiculos, lista_de_clientes, lista_de_faturas = carrega_as_listas_dos_ficheiros()

        elif op == "nc":
            novo_cliente = cria_novo_cliente()
            if novo_cliente is not None:
                lista_de_clientes.append(novo_cliente)

        elif op == "nv":
            novo_veiculo = cria_novo_veiculo()
            if novo_veiculo is not None:
                lista_de_veiculos.append(novo_veiculo)

        elif op == "nf":
            if len(lista_de_clientes) == 0 or len(lista_de_veiculos) == 0:
                print("Não há clientes ou veiculos registados...")
                continue

            nova_fatura = cria_nova_fatura(lista_de_clientes, lista_de_veiculos)
            lista_de_faturas.append(nova_fatura)

        elif op == "lc":
            imprime_lista_de_clientes(lista_de_clientes)
            pause()

        elif op == "lv":
            imprime_lista_de_veiculos(lista_de_veiculos)
            pause()

        elif op == "lf":
            imprime_lista_de_faturas(lista_de_faturas)
            pause()

if __name__ == "__main__":
    menu()
