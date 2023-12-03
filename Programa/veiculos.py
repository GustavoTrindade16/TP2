from io_terminal import imprime_lista

nome_ficheiro_lista_de_veiculos = "lista_de_veiculos.pk"

def imprime_lista_de_veiculos(lista_de_veiculos):
    #Prints the list of vehicles formatted.

    #This function receives a list of vehicles and prints their data in a formatted format.
    #in the terminal, using the `imprime_lista` function of the `io_terminal` module.

    #:param vehicle_list: List of vehicles to be printed.
     #                         Each vehicle is represented as a dictionary.
      #                        Example: [{"brand": "Toyota", "registration": "AB123CD", ...}, {...}, ...]
    
    imprime_lista(cabecalho="Lista de Veículos", lista=lista_de_veiculos)

def cria_novo_veiculo():
    #Asks the user to enter a new vehicle.

    #:return: Dictionary with new vehicle data.
     #        Example: {"brand": "Toyota", "registration": "AB123CD", ...}
    
    marca = input("marca? ")
    matricula = input("matricula? ").upper()
    # TODO: Pedir o resto dos dados do veículo, e não esquecer de guardá-los no dicionário
    # ...

    veiculo = {"marca": marca,
               "matricula": matricula}

    return veiculo
