print('-'*100)
print()
print('Você se encontra perdido e confuso...\nah uma luz mais a frente...\n')
# escolha de rota
while True:
    escolha = input('oque você quer fazer?:')
    match escolha:
        case 'me matar':
            print('Você morre.(não sei oq vc tava esperando mas ok.)')
            break
        case 'esperar':
            print('Você fica parado, esperando talvez que magicamente apareça alguém para oh ajudar, mas você percebe enfim que ninguém virá. A única pessoa que pode te salvar é você mesmo.')
        case 'seguir em frente':
# escolha de equipamento
            print('Você decide seguir a luz que ilumina o caminho a frente...\nVocê vê então uma espada e um escudo no chão...\nVocê não tem forças para carregas as duas...\nDeve escolher apenas uma...')
            arma = input('Qual delas você levará?')
            while True:
                match arma:
                    case 'espada':
                        print(
                            'Você pega do chão uma espada velha e enferrujada de cobre, não é o ideal, mas pode fazer estrago.')
                        break
                    case 'escudo':
                        print('Você se agacha para pegar um escudo redondo feito de madeira, a madeira que componhe o escudo parece desgastada e frágil, porém ainda aguenta o tranco.')
                        break
                    case 'nenhuma':
                        print('Talvez, buscando se desafiar, ou talvez, a fadiga tenha retirado de você o único pingo de bom senso que ainda restava, você decide então não levar nenhum deles. Boa sorte.')
                        break
                    case _:
                        print('Não é uma opção')
# inimigo
            print('houie')
            break
        case _:
            print('Não é uma boa ideia.')
print()
print('-'*100)
