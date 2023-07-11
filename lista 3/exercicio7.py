#Faça um programa que leia 100 números inteiros e diga qual é o menor.
for i in range(1,6,1):
    n=int(input('Entre com um número:\n'))
    if (i==1):
        menor=n
    else:
        if (n<menor):
            menor=n
print (f'o menor número é {menor}')
