##resolucao Guanabara
##para evitar os espaços desnecessarios (de antes ou depois), usa a funcao "strip"
nome = str (input ("Digite seu nome completo: ")).strip()
print ("Analisando seu nome...")
print ("Seu nome em maisculo é {}".format (nome.upper()))
print ("Seu nome em minusculo é {}".format (nome.lower()))
#agora para eliminar os espacos, ou nao fazer o "len" contar os espacos, usa o (menos) count espaço, 
print ("Seu nome tem ao todo {} letras".format (len(nome) - nome.count (" ")))
print ("Seu primeiro nome tem {} letras".format (nome.find (" ")))
