from math import sqrt
print ("\033[1;43m\n","=-"*21,"\nAPRENDA EQUAÇÃO SEGUNDO GRAU - PASSO A PASSO\n","-="*21,"\033[m")
print ("\033[33mEquação: ax² + bx + c = 0\n\033[m\n\n")

print ("\033[41mPARA COMEÇAR PRECISAMOS DOS VALORES DE 'a,b,c'\033[m\n")
a = float (input ("\033[31mInsira o valor de 'a': "))
b = float (input ("Insira o valor de 'b': "))
c = float (input ("Insira o valor de 'c': "))
print ("\033[m\n")
print ("\033[42;1mFORMULA DE BHASKARA\033[m")
print ("\033[32;4m-b +- √∆\033[m")
print ("\033[32m2 * a")
print ("\n∆ = b² -4 * a * c\n∆ = delta\n\033[m\n")

print("\033[7mInicia resolvendo os valor de delta, dentro da raiz:\n\033[m")
print ("∆ = b² -4*a*c\n")
print ("b²= %.2f\n" % (b**2))
print ("%.2f -4*(%.2f*%.2f)\n" % ((b**2),a,c))
print ("%.2f -4*%.2f\n" % ((b**2),(a*c)))
print ("%.2f %.2f\n" % ((b**2),(-4*(a*c))))
delta = ((b**2)+(-4*(a*c)))
print (delta)

print ("\033[44m\nAgora só podemos continuar a operação se delta for maior que 0. Pois nao é possível tirar raiz de 0 ou de número negativo. Se não for o programa ira escrever que é 'impossivel calcular'.Se você estiver fazendo no caderno, pode escrever que é impossível calcula\n\033[m")
print ("\033[m\033[2m∆ = %.2f\n\033[m" % (delta))
if delta > 0: 
    
    print ("√∆= %.2f\n\033[m" % (sqrt(delta)))
    delta = sqrt(delta)
    print ("\033[45mExistem 2 possíveis incógnitas que solucionam a equação, sendo elas x1 e x2. Para chegarmos aos de x1 e x2, usaremos o resto da formula a esquerda da raiz, e dividir por 2*a\n\nx1 usaremos o '+' da fórmula\n\033[m")
    print ("\033[35m\nx1 = (-b + √∆)/(2*a)")
    print ("\nx1 = (-(%.2f)+%.2f) / (2*%.2f)" % (b,delta,a))
    print ("\nx1 = %.2f / %.2f" % (((-b)+delta),(2*a)))
    x1 = ((-(b))+delta)/(2*a)
    print ("\n\033[1mx1 = %.2f\n\033[m" % (x1))
    print ("-"*10)

    print ("\033[45m\n\nx2 usaremos o '-' da fórmula\n\033[m")
    print ("\033[35m\nx2 = (-b - √∆)/(2*a)")
    print ("\nx2 = (-(%.2f)-%.2f) / (2*%.2f)" % (b,delta,a))
    print ("x2 = %.2f / %.2f" % (((-b)-delta),(2*a)))
    x2 = (((-(b))-(delta))/(2*a))
    print ("\n\033[1mx2 = %.2f\n\033[m" % (x2))

    print ("\033[7mPARA TESTAR SE OS RESULTADOS ESTÃO CERTOS, PEGA X E COLOCA NA EQUAÇÃO, SE O RESULTADO FINAL FOR ZERO, ENTÃO ESTA CORRETO\033[m")
    print ("\na = %.2f\nb = %.2f\nc = %.2f" % (a,b,c))
    print ("\nx1 = %.2f" % (x1))
    print ("x2 = %.2f" % (x2))
    print ("\nax² + bx + c = 0")
    res = (a*(x1**2))+(b*x1)+c
    print ("(%.2f(%.2f²))+(%.2f*%.2f)+%.2f = %.2f" % (a,x1,b,x1,c,res))

    res = (a*(x2**2))+(b*x2)+c
    print ("(%.2f(%.2f²))+(%.2f*%.2f)+%.2f = %.2f" % (a,x2,b,x2,c,res))

else:
    print ("="*21,"\nImpossível Calcular\n","="*21)