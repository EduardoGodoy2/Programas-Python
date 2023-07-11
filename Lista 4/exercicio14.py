# Faça um programa que leia um número inteiro n qualquer e mostre na tela a figura abaixo.
n=int(input('Entre com um número:\n'))
i=1
while (i<=n):
    j=1
    while (j<=i):
        print('*', end="")
        j+=1
    print()
    i+=1