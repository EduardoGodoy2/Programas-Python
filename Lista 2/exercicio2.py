# Faça um programa que leia um número, e se ele for maior que 20 então imprima metade do número, caso contrário imprima o dobro do valor.
n=int(input('Entre com um número:\n'))
if (n>=20):
    print(f'{n//2}')
else:
    print(f'{n*2}')