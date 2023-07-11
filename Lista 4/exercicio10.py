# Faça um programa que leia um número inteiro e  calcule o seu fatorial.
i=1
fat=1
n=int(input('Entre com um número:\n'))
while (i<=n):
    fat*=i
    i+=1
print(f'O fatorial de {n} é {fat}')