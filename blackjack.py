from random import randint
import time
import os

def clear():
    os.system('clear')

def game():
    carta1 = randint(1, 10)
    print('Carta 1: ' + str(carta1))
    carta2 = randint(1, 10)
    print('Carta 2: ' + str(carta2))
    soma = carta1 + carta2
    print ('Ate agora voce tem: ' + str(soma))

    while soma <= 21:
        i = 3
        if soma == 21:  break

        escolha = input("Deseja escolher outra carta? [y/n]")

        if escolha == 'y':
            carta = randint(1, 10)
            print('Carta ' + str(i) + ': ' + str(carta))
            soma = soma + carta
            i = i + 1
            print ('Ate agora voce tem: ' + str(soma))
        else:
            break
    if soma > 21: print('Infelizmente voce estourou sua pontuacao :( ')
    print(" Seus pontos:  " + str(soma))
    time.sleep(3)
    return soma

def message(jogador):
    print('------------------------------')
    print('---- Iniciando jogador ' + str(jogador) +  '-----')
    print('------------------------------')

def print_result(j1,j2):
    if j1 > 21 and j2 > 21: print('Jogo empatado os dois estouraram j1:' + str(j1) + ' ,j2: ' + str(j2))
    elif j1 > 21 : print('Jogador 1 estourou:' + str(j1) + '; Jogador 2 ganhou!')
    elif j2 > 21 : print('Jogador 2 estourou:' + str(j2) + '; Jogador 1 ganhou!')
    elif j1 == j2: print('Jogo empatado em ' + str(j1) + ' a ' + str(j2))
    elif j1 > j2: print('Jogador 1 ganhou ' + str(j1) + ' a ' + str(j2))
    elif j2 > j1: print('Jogador 2 ganhou ' + str(j2) + ' a ' + str(j1))

message(1)
j1 = game()
clear()
message(2)
j2 = game()
clear()

print_result(j1,j2)
