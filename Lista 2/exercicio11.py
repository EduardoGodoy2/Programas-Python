#Faça um programa que leia um número e diga se ele é divisível por 3 e por 7. Obs.: utilize operador lógico.
n=int(input('Entre com um número:\n'))
if (n%3==0) and (n%7==0):
    print(f'{n} é divisivel por 3 e 7.')
else:
    print(f'{n} não é divisivel por 3 e 7.')