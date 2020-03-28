#Exercício Python #103 - Ficha do Jogador
#Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

print(30*'-')


def ficha(nome=0, gols=0):
    if nome == '':
        nome = '<desconhecido>'
    
    try:
        gols = int(gols)
    except ValueError:
        gols = 0
    
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')

nome = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols: '))

ficha(nome,gols)

