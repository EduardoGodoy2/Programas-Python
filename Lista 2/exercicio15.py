# Faça um programa que leia um número inteiro de 3 dígitos e 
# informe se o algarismo da casa das centenas é par ou ímpar.
n=int(input('Entre com um número de 3 digitos:\n'))
num=str(n)
a=len(num)
if (a!=3):
    print('Error!')
elif((n//100)%2==0):
    print(f'a centena de {n} é par.')
else:
    print(f'a centena de {n} é impar.')