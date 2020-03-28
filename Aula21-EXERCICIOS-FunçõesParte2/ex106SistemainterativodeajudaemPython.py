#Exercício Python #106 - Sistema interativo de ajuda em Python
#Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.

from time import sleep

def verde(texto):
    print('\033[0;30;42m'+(len(texto)+4)*'~')
    print('  '+texto+'  ')
    print((len(texto)+4)*'~')

def azul(texto):
    print('\033[0;30;44m'+(len(texto)+4)*'~')
    print('  '+texto+'  ')
    print((len(texto)+4)*'~')


def vermelho(texto):
    print('\033[0;30;41m'+(len(texto)+4)*'~')
    print('  '+texto+'  ')
    print((len(texto)+4)*'~')


def ajuda(texto):
    print('\033[m'+'\033[7;30m')
    help(texto)


while True:
    verde('SISTEMA DE AJUDA PyHELP')
    escolha = input('\033[mFunção ou Biblioteca > ').lower()
    if escolha in 'fim':
        vermelho('ATÉ LOGO')
        sleep(1)
        break

    azul(f"Acessando o manual do comando '{escolha}'")
    sleep(1)

    ajuda(escolha)