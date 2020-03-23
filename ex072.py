#-*-coding:utf8;-*-
#qpy:3
#qpy:console
while True:
    user = int(input('Digite um número entre 0 a 20: '))
    if user >= 0 and user <=20:
        break

numero = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

for c in range(0,len(numero)):
    if c == user:
        print(numero[c])
