# Faça um programa que leia 5 números inteiros e diga qual é o menor.
i=1
while (i<=5):
    n=int(input('Entre com um número:\n'))
    if (i==1):
        menor=n
    elif (n<menor):
        menor=n
    i+=1
print(f'O menor número é {menor}')