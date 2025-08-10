# Fusão de divisoria.
def D():
    print('-'*30)

# Função exibição.


def L():
    for liste in lista:
        print(liste)

# Função junta funções.


def LD():
    "Função que junta funções"
    L()
    D()


print()
print('Dados do primeiro usuario')
print()

# Criei um dicionario com registro de nome, email e telefone do usuario.
Dados1 = {
    "Nome": "Joãozinho",
    "Email": "joaozinhodopneu123@gmail.com",
    "Telefone": "9999-9999"
}

# Print para mostrar as informações do dicionario.
for k, v in Dados1.items():
    print(f'O {k} é {v}!')

D()


# Gerei mais um usuario.
Dados2 = {
    "Nome": 'Frederico',
    "Email": 'FredericoFazber@gmail.com',
    "Telefone": '4002-8922'
}

# Criei e adicionei os dois dicionarios criados até o momento dentro de uma lista.
lista = [Dados1, Dados2]
print(lista)

D()

LD()

print('Vamos cadastrar um novo usuario!!')
print()

# (Metodo de inclusão de novos registros)
# Gerei um novo dicionario vazio.
Dados3 = {}

# Esse codigo tem a função de adicionar um novo conjunto de dados para a lista, eu espeficamente escolhi adicionar dados para uma unica pessoa, mas sim, poderia ter feita para adicionar mais de uma.
#   / Dados3["Nome"] = Dentro da chave (nome),  input("Digite o seu nome!") = ele vai adicionar o valor em string que o usuario adicionar aqui.
Dados3["Nome"] = input("Digite o seu nome!")
Dados3["Email"] = input("Me diga seu email!")
Dados3["Telefone"] = input("Insira seu contato Celular!")

# Adicionar os dados3 dentro da lista.
lista.append(Dados3)

D()
print('(Dados3) Adicionado com susseso!.')
print()

# Conferir se realmente os dados3 foram adicionados (!spoiler!, foram sim).

LD()

# Alteração no Dados1 (não dinamica).
print('(Dados1) atualizados!')
print("")

Dados1["Nome"] = ("Nome generico")
Dados1["Email"] = ("Email generico")
Dados1["Telefone"] = ("Telefone generico")

LD()

# Atualizar Dados1 (com input).
print('Alterar (Dados1)')
print()

Dados1["Nome"] = input("Alterar nome")
Dados1["Email"] = input("Alterar Email")
Dados1["Telefone"] = input("Alterar Telefone")

D()

print('(Dados1) atulaizados!')
print()

LD()

# Adicionando IDS.
print('IDS Adicionados com susseso!.')
print()

Dados1["ID"] = '01'
Dados2["ID"] = '02'
Dados3["ID"] = '03'

L()

# Confirmando que está funcionando (!spoiler denovo! está sim.)
print(type(Dados1['ID']))

D()

# Menu interativo.
while True:
    Escolha = (input('Oque deseja fazer?. \n 01 = Editar um registro \n 02 = Deletar algum registro \n 03 = Adicionar um novo registro \n 04 = Sair.'))
    if Escolha == '1':
        Registro = input('Deseja editar o registro de quem?')
        if Registro == '1':
            Dados1["Nome"] = input("Alterar nome")
            Dados1["Email"] = input("Alterar Email")
            Dados1["Telefone"] = input("Alterar Telefone")
            print('Dados1 foram atualizados.')
        elif Registro == '2':
            Dados2["Nome"] = input("Alterar nome")
            Dados2["Email"] = input("Alterar Email")
            Dados2["Telefone"] = input("Alterar Telefone")
            print('Dados2 foram atualizados.')
        elif Registro == '3':
            Dados3["Nome"] = input("Alterar nome")
            Dados3["Email"] = input("Alterar Email")
            Dados3["Telefone"] = input("Alterar Telefone")
            print('Dados3 foram atualizados.')

    # Deletar os dados através do ID.
    elif Escolha == '2':
        Deletar = input(
            "Você que deletar os dados de quem? (ex: 1 = Dados1, 2 = Dados2)")

        if Deletar == '2':
            Dados2.pop('Email')
            Dados2.pop('Nome')
            Dados2.pop('Telefone')
            Dados2.pop('ID')
            print('Dados2 removido.')
        elif Deletar == '1':
            Dados1.pop('Email')
            Dados1.pop('Nome')
            Dados1.pop('Telefone')
            Dados1.pop('ID')
            print('Dados1 removido.')
        elif Deletar == '3':
            Dados3.pop('Email')
            Dados3.pop('Nome')
            Dados3.pop('Telefone')
            Dados3.pop('ID')
            print('Dados3 removido.')
        else:
            print('Infelizmente, não identifeiquei esse registro.')
    # Adicionar um novo registro.
    elif Escolha == '3':
        Dados4 = {}
        Dados4["Nome"] = input("Digite o seu nome!")
        Dados4["Email"] = input("Me diga seu email!")
        Dados4["Telefone"] = input("Insira seu contato Celular!")
        Dados4["ID"] = '04'
        lista.append(Dados4)
        print('Dados4 foi adicionado ao registro.')
        LD()
    # Não fazer nada.
    elif Escolha == '4':
        D()
        print('Adeus!!')
        D()
        break
    # Erro no codigo
    else:
        print('ISSO NÂO, BURRO, ESTUPIDO.')

    D()
