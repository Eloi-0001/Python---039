import func
lista_registros = []


while True:
    escolha = input(
        'Bom dia. \n 01 = Criar um registro. \n 02 = Editar um registro. \n 03 = Excluir um registro. \n 04 = Visualizar os registros. \n 05 = Sair.\n:')
    if escolha == "1" or escolha == "01" or escolha == "um" or escolha == "Um":
        func.registro_dados(lista_registros)
        print('Registro criado com sucesso!')
    elif escolha == "2" or escolha == "02" or escolha == "dois" or escolha == "Dois":
        func.editar_dados(lista_registros)
        print('Dados editados com sucesso!')
    elif escolha == "3" or escolha == "03" or escolha == "tres" or escolha == "Tres" or escolha == "três" or escolha == "Três":
        func.deletar_dados(lista_registros)
        print('Dados deletados com sucesso!')
    elif escolha == "4" or escolha == "04" or escolha == "quatro" or escolha == "Quatro":
        for registros in lista_registros:
            print(registros)
    else:
        print('Adeus')

        break
