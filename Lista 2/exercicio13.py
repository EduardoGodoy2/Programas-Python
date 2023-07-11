# Faça um programa que leia um número e diga se ele está compreendido entre 20 e 90 ou não.
n=int(input('Entre com um número:\n'))
if (n>=20) and (n<=90):
    print(f'{n} é um número compreendido.')
else:
    print(f'{n} não é um número compreendido.')