#Faça um programa que imprima a raiz quadrada de um número caso ele seja positivo e o quadrado do número caso ele seja negativo.
n=int(input('Entre com um número:\n'))
if (n>0):
    print(f'{n} é positivo e sua raiz quadrada é {n**0.5:.1f}')
else:
    print(f'{n} é negativo e seu valor ao quadrado é {n**2}')