#Faça um programa que leia dois lados de um triângulo retângulo e calcule a hipotenusa
a=int(input('Entre com um lado do triângulo:\n'))
b=int(input('Entre com o outro lado do triângulo:\n'))
c=(a**2)+(b**2)
print(f'Sua hipotenusa é {c}')