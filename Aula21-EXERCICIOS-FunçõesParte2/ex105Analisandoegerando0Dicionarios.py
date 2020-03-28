#Exercício Python #105 - Analisando e gerando Dicionários
#Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

#- Quantidade de notas
#- A maior nota
#- A menor nota
#- A média da turma
#- A situação (opcional)

#Adicione também as docstrings dessa função para consulta pelo desenvolvedor."""


#DEFININDO A FUNCAO:
def notas(*n,sit=False):
    """-> Função para analisar notas e situações de vários alunos.
    :parametro n: uma ou mais notas dos alunos(aceita várias)
    :parametro sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """

    n = n
    resul = {'total': 0, 'media': 0}
    for c in n:
        resul['total'] += 1
        resul['media'] += c
    resul['media'] = resul['media']/resul['total']
    resul['maior'] = max(n)
    resul['menor'] = min(n)

    if sit == True:
        if resul['media'] < 5:
            resul['situação'] = 'RUIM'
        elif resul['media'] > 5 and resul['media'] < 7:
            resul['situação'] = 'RAZOAVEL'
        else:
            resul['situação'] = 'BOA'

    return resul


#PROGRAMA PRINCIPAL
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)