#Faça um programa que leia um número e diga se ele é divisível por 3 e por 7. 
# Obs.: Não é permitido a utilização de operador lógico. 
# Se o número for divisível por 21 ele então é divisível por 3 e por 7.
n=int(input('Entre com um número:\n'))
if (n%21==0):
    print(f'{n} é divisivel por 3 e 7.')
else:
    print('não é divisivel por 3 e 7.')