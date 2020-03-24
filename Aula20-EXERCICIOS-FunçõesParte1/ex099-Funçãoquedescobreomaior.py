from time import sleep

def maior(*num):
    print(20*'=-')
    print('Analisando os valores passados...')
    if len(num) > 0:
        for c in num:
                print(c,end=' ',flush=True)
                sleep(0.5)
        print(f'Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi {max(num)}.')
    else:
        print(f'Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi {len(num)}.')
        
maior(0,0,6,8,6,5,8)
maior()