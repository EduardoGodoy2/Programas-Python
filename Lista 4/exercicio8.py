# Faça um programa que leia 5 números inteiros e diga quantos são ímpares.
i=1
cont=0
while (i<=5):
    n=int(input('Entre com um número:\n'))
    if (n%2==1):
        cont+=1
    i+=1
print(cont)