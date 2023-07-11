#Faça um programa que leia dois valores A e B e em seguida efetue a troca dos valores de forma que a variável A passe a ter o valor da variável B e vice e versa.
from calendar import c


a=float(input('Entre com um valor:\n'))
b=float(input('Entre com outro valor:\n'))
c=a
a=b
b=c
print(f'{a} {b}')