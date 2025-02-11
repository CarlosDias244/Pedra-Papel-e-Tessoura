import random

def play():
    jogo = True
    partidas = 0
    derrota = 0
    empate = 0
    vitoria = 0

    while jogo:

        user = input("O que escolher? 'r' para rocha, 't' para tessoura, 'p' para papel\n>>> ")
        computer = random.choice(['p','r','t'])
        print(f'PC {computer}')

        if computer == 'p':
            print('O computador jogou PAPEL')

        elif computer == 'r':
            print('O computador jogou ROCHA')

        else:
            print('O computador jogou TESOURA')

        if user == computer:
            print('Empate')
            empate += 1

        elif (user == 't' and computer == 'r') or (user == 'p' and computer == 't') or (user == 'r' and computer == 'p'):
            print('\033[0;31mVocê Perdeu!\033[m')
            derrota += 1

        elif (user == 'r' and computer == 't') or (user == 't' and computer == 'p') or (user == 'p' and computer == 'r'):
            print('\033[0;32mVocê Ganhou!\033[m')
            vitoria += 1

        else:
            print('\033[2;34mOpção inválida.\033[m')
            return play()

        partidas += 1

        continuar = int(input('Deseja jogar novamente?\n[1] Sim\n[2] Não\n>>>'))

        if continuar == 1:
            continue

        elif continuar == 2:
            print(f"Em um total de {partidas} partidas, você ganhou {vitoria}, perdeu {derrota} e empatou {empate}.")
            jogo = False

play()