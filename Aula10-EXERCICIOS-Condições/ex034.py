sal = float (input ("Digite seu salario: "))
if sal < 1250:
    aum = sal*0.15
else:
    aum = sal*0.1
print ("Você terá um aumento de R$ %.2f" % (aum))