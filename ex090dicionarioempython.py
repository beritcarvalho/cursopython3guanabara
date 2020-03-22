#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela
aluno = dict()
aluno['Nome'] = str(input('Nome: '))
print(aluno)
aluno['Media'] = float(input('Media: '))
if aluno['Media'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'

for chave,valor in aluno.items():
    print(f'{chave} é {valor}')

