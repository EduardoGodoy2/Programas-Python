# Faça um programa que leia um número inteiro e calcule e mostre os n primeiros termos da série de Fibonacci. 
n=int(input('Entre com um número:\n'))
t1=0
t2=0
tatual=1
i=1
while (i<=n):
    print(tatual, end=" ")
    t1=t2
    t2=tatual
    tatual=t1+t2
    i+=1