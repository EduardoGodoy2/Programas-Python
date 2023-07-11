# Faça um programa que leia 3 números e diga se eles podem ou não formar um triângulo, caso afirmativo, 
# diga se o  triângulo é equilátero isósceles ou escaleno.
num1=int(input('Entre com um número:\n'))
num2=int(input('Entre com um número:\n'))
num3=int(input('Entre com um número:\n'))
maior=num1
if (maior<num2):
    maior=num2
if (maior<num3):
    maior=num3
elif (maior==num1):
    if (num2+num3>num1):
        print(f'{num2} + {num3} podem formar um triângulo')
elif (maior==num2):
    if (num1+num3):
        print(f'{num1} + {num3} podem formar um triângulo')
elif (maior==num3):
    if (num2+num1):
        print(f'{num2} + {num1} podem formar um triângulo')
if (num1==num2) and (num1==num3):
    print('é um triangulo equilátero.')
if (num1==num2) and (num2!=num3):
    print('é um triângulo isósceles.')
if (num1!=num2) and (num2!=num3) and (num1!=num3):
    print('é um triângulo escaleno.')