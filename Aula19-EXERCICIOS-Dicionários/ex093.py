#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = dict()
jogador['nome'] = str(input('Nome do Jogador: '))
print(jogador)
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
jogador['gols'] = list()

for p in range(0,partidas):
    gol = int(input(f'Quantos gols na partida {p} '))
    jogador['gols'].append(gol)

print(20*'=-')

print(jogador)

jogador['total']=0
for pos,v in enumerate(jogador['gols']):
    jogador['total'] += v


print(20*'=-')

for chave,valor in jogador.items():
    print(f'O campo {chave} tem o valor {valor}')

print(20*'=-')

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for c in range(0,partidas):
    print(f'    => Na partida {c}, fez {jogador["gols"][c]} gols.')

print(f'Foi um total de {jogador["total"]} gols.')