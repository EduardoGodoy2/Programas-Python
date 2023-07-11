# Faça um programa que leia um número inteiro n qualquer e mostre na tela a figura abaixo. 
n=int(input('Entre com um número:\n'))
for i in range(1,n+1):
    j=1
    for j in range(1,i+1):
        print('*', end =" ")
    print()