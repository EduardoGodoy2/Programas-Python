# Faça um programa que mostre a tabuada de 1 até 10 de um número inteiro lido do teclado. 
# O resultado deve aparecer da seguinte forma: 
# Se o número lido for 5.1 x 5 = 5
# 2 x 5 = 10...
# 10 x 5 = 50
n=int(input('Entre com um número:'))
i=1
while (i<=10):
    m=i*n
    print(f'{i} x {n} = {m}')
    i+=1