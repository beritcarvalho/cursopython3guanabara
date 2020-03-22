#Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter


print('Valores sorteados: ')
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6),      
        }

for chave,valor in jogo.items():
    print(f'O {chave} tirou {valor}')
    sleep(0.5)


print('\nRanking dos jogadores: ')

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for posicao, valor in enumerate(ranking):
    print(f'{posicao+1}° lugar: {valor[0]} com {valor[1]}')