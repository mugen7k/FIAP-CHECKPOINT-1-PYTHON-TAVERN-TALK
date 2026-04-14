import random

player_coins = 77

print('Você avista a fumaça da taverna de longe. Realmente um hidromel não iria mal, seria ótimo para esquentar em meio àquela noite fria.')

#ENTRADA NA TAVERNA
while True:
    print()
    print('Você chega à porta da taverna.')
    print('1 = Entrar')
    print('2 = Olhar a janela')
    print()
    entrar_na_taverna = input('O que você faz?: ')

    if entrar_na_taverna == '1':
        break
    elif entrar_na_taverna == '2':
        print()
        print('Você olha lá dentro e vê vários homens rindo e brindando. Parece um lugar muito aconchegante.')
print('Você empurra aquela porta pesada, a atravessa, e logo uma onda de calor atinge seu corpo.')

#RECEPÇÃO
print('Em seguida um homem bêbado esbarra em você, ele nem se preocupa em pedir desculpas. Em seguida você vai até o balcão. Um homem careca, barbudo e parrudo se aproxima para te atender:')
print('"Qual o seu nome jovem?" Indaga o velho careca e barbudo')
print()

player_name = str(input('Me chamo... '))
print()

print(f'"De que bandas você vem {player_name}?"')
print('1 = Montanhas Milenares')
print('2 = Litoral Lamuriante')
print('3 = Vale Venerável')
print('4 = Cidade Cinzenta')
print('5 = Lugar nenhum!')
print()

player_history = int(0)
while not (1<= player_history <= 5):
    player_history = int(input('Responda: '))
print()

match player_history:
    case 1 | 3:
        print('"Ha, já imaginava. Essa cara de bebê não engana ninguém! Haha!😏"')
    case 2 | 4:
        print('"Hmm, já ouvi muitos relatos sombrios dessas bandas. Você parece muito conservado para ter vindo de lá. 🤔"')
    case 5:
        print('"Ahh vai ser assim então. Ok.😑"')

#SALÃO
print(f'"Me chamo Candidus, sou dono deste estabelecimento. Não me arrume confusão aqui {player_name}, senão irá conhecer meu lado não tão receptivo."')
print()
while True:

    print('"Fique à vontade jovem. Aliás, vai querer algo para animar essa cara feia?"')
    print()
    print('1 = Pedir uma bebida ou comida no balcão')
    print('2 = Ir até o viajante')
    print('3 = Enfrentar o bêbado')
    print('4 = Ir até o bardo')
    print('5 = Ir a mesa de jogos')
    print('6 = Falar com o caçador de recompensas')
    print('7 = Ir embora e seguir sua jornada')
    print()
    player_action = str(input('"E aí, o que vai querer?:" '))
    print()

    match player_action:

        # BARISTA (COMIDAS E BEBIDAS)
        case '1':
            while True:
                print('Você permanece no balcão')

        # VIAJANTE (VENDEDOR DE MAPAS)
        case '2':
            while True:
                print('Você vai até o viajante')

        # BÊBADO
        case '3':
            while True:
                print('Você vai em direção ao bêbado')

        # BARDO (MÚSICA)
        case '4':
            while True:
                print('Você vai até o direção ao bardo')

        # JOGADOR DE DADOS (MINI GAME)
        case '5':
            while True:

                print('Você senta à mesa de jogos')
                print()
                print('"Eai forasteiro, quer tentar a sorte? É só jogar os dados, o maior número leva o ouro!"')
                print('1 = Apostar')
                print('2 = Verificar o número de moedas')
                print('3 = Voltar ao balcão')
                print()
                decisao_mesa_de_jogos = input('O que irá fazer?: ')
                print()

                match decisao_mesa_de_jogos:

                    case '1':
                        if player_coins >= 1:
                            aposta_player = int(player_coins + 1)

                            while aposta_player > player_coins:
                                print('"Quanto dinheiro vai apostar mané?"')
                                aposta_player = int(input('Vou apostar: '))

                            if aposta_player == player_coins:
                                print('"Tudo isso?!"')

                            print('"Hua hua, vamos lá. Você primeiro..."')
                            print('Você joga os dados...')
                            dado_player_1 = random.randint(1, 6)
                            dado_player_2 = random.randint(1, 6)
                            soma_dados_player = dado_player_1 + dado_player_2
                            print(f'Você tirou {dado_player_1} e {dado_player_2}. A soma é {soma_dados_player}')
                            dado_npc_1 = random.randint(1, 6)
                            dado_npc_2 = random.randint(3, 6)
                            soma_dados_npc = dado_npc_1 + dado_npc_2
                            print(f'O estranho tirou {dado_npc_1} e {dado_npc_2}. A soma é {soma_dados_npc}')

                            if soma_dados_npc > soma_dados_player:
                                print()
                                print('"Hahaha, talvez você tenha mais sorte da próxima vez"')
                                player_coins = player_coins - aposta_player
                                print()
                                print(f'Você perdeu {aposta_player} moedas')
                            elif soma_dados_npc < soma_dados_player:
                                print()
                                print('"Você está com sorte jovem"')
                                player_coins = player_coins + aposta_player
                                print()
                                print(f'Você ganhou {aposta_player} moedas')
                            else:
                                print('"Olha! Parece que empatamos"')

                        else:
                            print('"Parece que você está sem dinheiro seu zé ruela hahaha!"')

                    case '2':
                        if player_coins == 0:
                            print(f'Não sobrou nada...')
                        elif player_coins == 1:
                            print(f'Você só tem mais uma moeda.')
                        else:
                            print(f'Você tem {player_coins} moedas.')

                    case '3':
                        print('"Chega de apostar!"')
                        print('Você volta ao balcão')
                        break

        # CAÇADOR DE RECOMPENSAS (VENDEDOR DE ARMAS E CONTRATOS)
        case '6':
            while True:
                print('Você senta na mesma mesa que o caçador de recompensas')

        # SAIR
        case '7':
            print('Você vai embora')
            break

print('Você atravessa a porta pesada, e enfrenta novamente o frio da noite.')













