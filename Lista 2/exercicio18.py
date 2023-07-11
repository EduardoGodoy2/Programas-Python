# Faça um programa que leia 5 números e identifique o maior e o menor.
a=int(input('Entre com um número:\n'))
b=int(input('Entre com um número:\n'))
c=int(input('Entre com um número:\n'))
d=int(input('Entre com um número:\n'))
e=int(input('Entre com um número:\n'))
maior=a
menor=a
if (maior<b):
    maior=b
if (menor>b):
    menor=b
if (maior<c):
    maior=c
if (menor>c):
    menor=c
if (maior<d):
    maior=d
if (menor>d):
    menor=d
if (maior<e):
    maior=e
if (menor>e):
    menor=e
print(f'O maior é {maior} e o menor é {menor}')