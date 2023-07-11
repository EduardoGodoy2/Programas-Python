#Faça um programa que leia um número e diga se ele é par ou ímpar.
n=int(input('Entre com número:\n'))
if (n%2==0):
    print(f'O número {n} é par.')
else:
    print(f'{n} é impar.')