# Faça um programa que leia um número inteiro e calcule e mostre os n primeiros termos da série de Fibonacci. 
t1=0
t2=0
tatual=1
n=int(input('Entre com um número:\n'))
for i in range(n):
    print(tatual)
    t1=t2
    t2=tatual
    tatual=t1+t2