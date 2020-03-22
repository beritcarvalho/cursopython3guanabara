#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
print(30*'-')
titulo = 'PALPITE MEGA SENA'
print(f'{titulo:^30}')
print(30*'-')

escolha = int(input('Quantos jogos você quer que eu sorteie? '))
print(3*'=-',f' SORTEANDO {escolha} JOGO(S) ',3*'-=')

jogos = list()
jogo = list()

from time import sleep
from random import randint

for c in range(0,escolha):
  cont = 0
  while True:
    num = randint(1,60)
    if num not in jogo:
      jogo.append(num)
      cont += 1
    else:
      num = randint(1,60)
      
      
      

    if cont == 5:
      jogo.sort()
      jogos.append(jogo[:])
      print(f'Jogo {c+1}: {jogo}')
      sleep(0.5)
      jogo.clear()
      break
