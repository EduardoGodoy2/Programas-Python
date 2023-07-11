#Faça um programa que leia um  número e diga se esse número é   positivo, negativo ou nulo.
n=int(input('Entre com um número:\n'))
if (n>0):
    print(f'{n} é positivo.')
elif (n<0):
    print(f'{n} é negativo.')
else:
    print(f'{n} é nulo.')