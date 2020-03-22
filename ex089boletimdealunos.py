#Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
alunos = list()
aluno = list()
while True:
  nome = str(input('Nome: '))
  nota1 = float(input('Nota 1: '))
  nota2 = float(input('Nota 2: '))
  aluno.append(nome)
  aluno.append(nota1)
  aluno.append(nota2)
  aluno.append(((nota1+nota2)/2))
  alunos.append(aluno[:])
  aluno.clear()
  

  escolha = str(input('Quer continuar [S/N] '))
  while  escolha != 'S' and escolha != 's' and escolha != 'N' and escolha != 'n':
    escolha = str(input('Quer continuar [S/N] '))
  if escolha in 'nN':
    break

print(15*'=-')

No='No.'
NOME= 'NOME'
MEDIA= 'MÉDIA'
print(f'{No:<5}{NOME:<20}{MEDIA:<5}')
print('-'*30)
for c in range(0,len(alunos)):
  print(f'{c:<5}{alunos[c][0]:<20}{alunos[c][3]:>5}')

print(15*'=-','\n')

while True:
  id_aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
  if id_aluno == 1:
    break
  print(f'Notas de {alunos[id_aluno][0]} são {alunos[id_aluno][1:3]}')