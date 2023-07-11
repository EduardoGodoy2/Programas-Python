#) Faça um programa que mostre a tabuada de 1 até 10 de um número inteiro lido do teclado. 
# O resultado deve aparecer da seguinte forma: Se o número lido for 5
# .1 x 5 = 52 x 5 = 10...10 x 5 = 50
n=int(input('Entre com um número:\n'))
r=0
for i in range (1,11,1):
    r=i*n
    print(f'{n} x {i} = {r}')