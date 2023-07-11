# Faça um programa que leia um número é verifique se ele é um número primo.
n=int(input('Entre com um número:\n'))
i=1
cont=0
while (i<=n):
    if (n%i==0):
        cont+=1
    i+=1
if (cont==2):
    print(f'{n} é um número primo.')
else:
    print(f'Não é um número primo.')
