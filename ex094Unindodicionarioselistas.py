#Exerc�cio Python 094: Crie um programa que leia nome, sexo e idade de v�rias pessoas, guardando os dados de cada pessoa em um dicion�rio e todos os dicion�rios em uma lista. No final, mostre: 
#A) Quantas pessoas foram cadastradas
#B) A m�dia de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da m�dia

cadastro = list()
pessoa = dict()

while True:
    pessoa['nome'] = str(input('Nome: '))
 
    pessoa['sexo'] = str(input('Sexo: [M/F] '))
    while pessoa['sexo'] != 'F' and pessoa['sexo'] != 'f' and pessoa['sexo'] != 'M' and pessoa['sexo'] != 'm':
      print('ERRO! Por favor, digite apenas M ou F.')
      pessoa['sexo'] = str(input('Sexo: [M/F] '))

    pessoa['idade'] = int(input('Idade '))

    cadastro.append(pessoa.copy())
    pessoa.clear()
    print(cadastro)

    resp = str(input('Quer continuar"? [S/N] '))
    while resp != 'S' and resp != 's' and resp != 'N' and resp != 'n':
        print('ERRO! Responda apenas S ou N.')
        resp = str(input('Quer continuar"? [S/N] '))
    if resp in 'Nn':
        break

print(25*'=-')
#A) Quantas pessoas foram cadastradas
print(f'A) Ao todo temos {len(cadastro)} pessoas cadastradas.')

#B) A média de idade
media = 0
for c,v in enumerate(cadastro):
    media += cadastro[c]['idade']
media = media/len(cadastro)
print(f'B) A média de idade é de {media:.2f} anos')

#C) Uma lista com as mulheres
print('C) As mulheres cadastradas foram',end=' ')
for pess in cadastro:
    if pess['sexo'] in 'Ff':
        print(pess['nome'], end=' ')
print('')

#D) Uma lista de pessoas com idade acima da média
print('Lista das pessoas que estão acima da média:')
for pess in cadastro:
    if pess['idade'] > media:
        for c,v in pess.items():
            print(f'{c} = {v}',end='; ')
        print('')
print('<< ENCERRADO >>')