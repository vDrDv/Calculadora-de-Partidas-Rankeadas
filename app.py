# Calculadora de Partidas Rakeadas

import random

win = random.randint(0, 201)
lose = random.randint(0, 101)

def saldo(win, lose):
    return win - lose

def nivel(win, lose):

    if win - lose == 10:
        return "Ferro"
    elif win - lose >= 11 and win - lose < 21:
        return "Bronze"
    elif win - lose >= 21 and win - lose < 51:
        return "Aço"
    elif win - lose >= 51 and win - lose < 81:
        return "Prata"
    elif win - lose >= 81 and win - lose < 91:
        return "Diamante"
    elif win - lose >= 91 and win - lose < 101:
        return "Lendário"
    elif win - lose >= 101:
        return "Imortal"
    else:
        return ": já pensou em jogar CSGO??"

vitoria = saldo(win, lose)
level = nivel(win, lose)

print("O Herói tem saldo de " + str(vitoria) + " está no nível " + str(level) + " !!!")