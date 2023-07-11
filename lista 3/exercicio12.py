# Faça um programa que leia um número é verifique se ele é um número primo.
cont=0
n=int(input('Entre com um número:\n'))
for i in range(1,n+1):
    if (n%i==0):
        cont+=1
if (cont==2):
    print(f'{n} é um número primo')
else:
    print(f'{n} não é um número primo')