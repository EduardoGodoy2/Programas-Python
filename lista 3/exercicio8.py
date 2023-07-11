# Faça um programa que leia 100 números inteiros e diga quantos são ímpares.
cont=0
for i in range(0,5,1):
    n=int(input('Entre com um número:\n'))
    if (n%2==1):
        cont+=1
print(cont)