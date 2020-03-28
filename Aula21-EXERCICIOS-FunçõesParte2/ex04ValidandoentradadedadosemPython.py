def leiaint(n):

    while True:
        try:
            n = int(n)
            break
        except ValueError:
            print('\033[0;31mERRO! Digite um numero inteiro válido.\033[m')
        n = input('Digite um numero: ')

    return n


num = leiaint('Digite um numero: ')
print(f'Você acabou de digitar o numero {num}')