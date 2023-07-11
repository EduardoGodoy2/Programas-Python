# Faça um programa que leia 100 números e diga quantos estão acima de 1000, quantos são iguais a 1000 e quantos estão abaixo de 1000.
c1=0
c2=0
c3=0
for i in range(0,5,1):
    n=int(input('Entre com um número:\n'))
    if (n>1000):
        c1+=1
    elif (n==1000):
        c2+=1
    else:
        c3+=1
print(f'{c1} estão acima de 1000, {c2} são iguais a 0 e {c3} estão abaixo de 1000 ')