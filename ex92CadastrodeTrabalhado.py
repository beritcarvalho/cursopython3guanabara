#Exerc�cio Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicion�rio. Se por acaso a CTPS for diferente de ZERO, o dicion�rio receber� tamb�m o ano de contrata��o e o sal�rio. Calcule e acrescente, al�m da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
ano_atual = date.today().year
cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano de Nascimento: '))
cadastro['idade'] = ano_atual-ano_nascimento
ctps = int(input('CTPS: (0 se não tiver) '))
print(30*'=-')

if ctps > 0:
    cadastro['ctps'] = ctps
    cadastro['contratação'] = int(input('Ano de Contratação: '))
    cadastro['salário'] = float(input('Salário: '))
    cadastro['aposentadoria'] = (cadastro['contratação']-ano_nascimento)+35

for c,v in cadastro.items():
    print(f'  - {c} tem o valorde {v}')