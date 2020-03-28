#Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
#from datetime import date
#ano_atual = date.today().year

def voto(ano_nascimento):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual-ano_nascimento
    if idade < 16:
        return print(f'Com {idade} anos: NÃO VOTA!')
    elif idade >= 16 and idade < 18:
        return print(f'Com {idade} anos: VOTO OPCIONAL!')
    elif idade >= 18 and idade < 65:
        return print(f'Com {idade} anos: VOTO OBRIGATÓRIO!')
    else:
        return print(f'Com {idade} anos: VOTO OPCIONAL!')


ano_nascimento = int(input('Digite o ano de nascimento: '))
voto(ano_nascimento)