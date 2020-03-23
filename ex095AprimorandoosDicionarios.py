time = list()
gols = list()
jogador = dict()

while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    #cada gol por partida
    for partida in range(1,(jogador['partidas'])+1):
        gols.append(int(input(f'Quantos gols na partida {jogador["partidas"]}? ')))
    jogador['gols'] = gols[:]

    #total de gols
    jogador['total_gols'] = 0
    for gol in jogador['gols']:
        jogador['total_gols'] += gol

    time.append(jogador.copy())

    #limpando variaveis
    gols.clear()
    jogador.clear()

    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()
        if resp[0] not in 'SN':
            print('ERRO! Apenas S ou N')
        else:
            break
    if resp[0] == 'N':
        break


#segunda parte dados do jogador
cod = 'cod'
n = 'nome'
g = 'gols'
t = 'total'
teste = 5
print(25*'=-')
print(f'{cod:<5}{n:<20}{g:<20}{t:>5}')
print(50*'-')

#Não da pra formatar lista, pra isso tem q tranforar ela em string
for ID, jog in enumerate(time):
    print(f'{ID:<5}{jog["nome"]:<20}{str(jog["gols"]):<20}{jog["total_gols"]:>5}')

print(50*'-')

#ultima parte
while True:
    escolha = int(input('Mostrar dados de qual jogador? (999 para parar) ')) 
    if escolha == 999:
        break
    if escolha >= len(time):
        print(f'ERRO! Não existe jogador com código {escolha}')
    else:
        print(' -- LEVANTAMENTO DO JOGADOR %s:' % time[escolha]['nome'])
        for pos,gol in enumerate(time[escolha]['gols']):
            print(f'    No jogo {pos+1} fez {gol} gols.')
print('<<VOLTE SEMPRE>>')