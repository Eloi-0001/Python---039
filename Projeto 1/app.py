
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

# Fusão de divisoria.


def D():
    print('-'*30)


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

# Função de organização.


def L():
    for liste in lista:
        print(liste)


L()

D()

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
lista.append(Dados3.copy())

D()
print('(Dados3) Adicionado com susseso!.')
print()

# Conferir se realmente os dados3 foram adicionados (!spoiler!, foram sim).
L()

D()

# Alteração no Dados1 (não dinamica).
print('(Dados1) atualizados!')
print("")

Dados1["Nome"] = ("Nome generico")
Dados1["Email"] = ("Email generico")
Dados1["Telefone"] = ("Telefone generico")

L()

D()

# Atualizar Dados1 (com input).
print('Alterar (Dados1)')
print()

Dados1["Nome"] = input("Alterar nome")
Dados1["Email"] = input("Alterar Email")
Dados1["Telefone"] = input("Alterar Telefone")

# Escolher qual dado deseja alterar.
Alterar = input('Deseja alterar dados de quem?')


D()

print('(Dados1) atulaizados!')
print()

L()


D()

# Adicionando IDS.
print('IDS Adicionados com susseso!.')
print()

Dados1["ID"] = int(('01'))
Dados2["ID"] = int(('02'))
# NOTA ESSA LINHA NÂO ESTÀ FAZENDO NADA. CORRIGIR FUTURAMENTE
Dados3["ID"] = int(('03'))

L()

# Confirmando que está funcionando (!spoiler denovo! está sim.)
print(type(Dados1['ID']))

D()

# Deletar os dados através do ID.

Deletar = int(input("Você que deletar os dados de quem?"))

if Deletar == 2:
    Dados2.pop('Email')
    Dados2.pop('Nome')
    Dados2.pop('Telefone')
    Dados2.pop('ID')

elif Deletar == 1:
    Dados1.pop('Email')
    Dados1.pop('Nome')
    Dados1.pop('Telefone')
    Dados1.pop('ID')

elif Deletar == 3:
    Dados3.pop('Email')
    Dados3.pop('Nome')
    Dados3.pop('Telefone')
    Dados3.pop('ID')

else:
    print('Infelizmente, não identifeiquei esse registro.')

D()

for liste in lista:
    if liste:
        print(liste)
