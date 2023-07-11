# Faça um programa que leia 5 números e diga quantos estão acima de 1000, quantos são iguais a 1000 e quantos estão abaixo de 1000.
i=1
cont=0
cont2=0
cont3=0
while (i<=5):
    n=int(input('Entre com um número:\n'))
    if (n>1000):
        cont+=1
    if (n==1000):
        cont2+=1
    if (n<1000):
        cont3+=1
    i+=1
print(f'{cont} estão acima de mil, {cont2} são iguais a mil, {cont3} são menos que mil')
