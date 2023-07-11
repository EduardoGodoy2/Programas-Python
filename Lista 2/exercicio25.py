#Faça um programa que leia um número binário de 4 digitos e diga quantos digitos zero existem nesse número
n=int(input('Entre com um número binário de 4 digitos.'))
cont=str(n)
len=len(cont)
zeros=0
if (len!=4):
    print('Error! Entre com um número binário de 4 DIGITOS.')
if (n%10==0):
    zeros+=1
if ((n//10)%10==0):
    zeros+=1
if ((n//100)%10==0):
    zeros+=1
if (n//1000==0):
    zeros+=1
print(f'Esse número binário possui {zeros} zeros')