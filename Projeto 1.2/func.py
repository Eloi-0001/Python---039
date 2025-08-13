def registro_dados(lista: list):
    "funão que gera dados de registro"
    registros = {}
    registros['nome'] = input('Insira nome?')
    registros['email'] = input('Insira email')
    registros['telefone'] = input('Insira telefone')
    lista.append(registros)


def deletar_dados(lista: list):
    "Função que deleta registros"
    ind = int(input("Qual registro da lista você deseja remover?"))
    lista.pop(ind)


def editar_dados(lista: list):
    "Função que edita registros"
    index = int(input("Qual registro da lista você deseja editar?"))
    registro = lista[index]
    chave = input("Qual campo você deseja alterar?")
    registro[chave] = input("Qual o novo valor?")


def exibir_dados(lista: list):
    "Apenas exibe a lista"

    for registro in lista:
        print(registro)
