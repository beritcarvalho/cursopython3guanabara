#Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint


jogador = dict()

for c in range(0,4):
    jogador['id'] = c+1
    jogador['dado'] = randint(1,6)
    print(f'Jogador{jogador["id"]} tirou {jogador["dado"]}')
    players = jogador.copy()
    jogador.clear

print(players)