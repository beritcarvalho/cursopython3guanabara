print("""COTAÇÃO DE VALORES\nDigite quantos Km será sua viagem.\nRegra de valores:\nViagens até 200Km, custam R$ 0.50 por km\nApartir dissto, custam R$ 0,45 por Km.\n""")
km = int (input ("Digite aqui o total de Km da sua viagem: "))
if km > 200:
    valor = km*0.45
    print ("O custo de passagem da sua viagem será de R$ %.2f" % (valor))
else:
    valor = km*0.50
    print ("O custo de passagem da sua viagem será de R$ %.2f" % (valor))