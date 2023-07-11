# Faça um programa que leia um caractere alfanumérico e diga se ele é uma vogal.
c=input('Entre com um caractere:\n')
aux=c
c=c.lower()
if (c=='a') or (c=='e') or (c=='i') or (c=='o') or (c=='u'):
    c=aux
    print(f'{c} é uma vogal.')
else:
    print(f'{c} não é uma vogal.')
