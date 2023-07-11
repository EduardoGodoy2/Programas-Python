#Faça um programa que leia os coeficientes de uma equação de segundo grau e devolva as raizes
n1=int(input('Entre com o primeiro coeficiente:\n'))
n2=int(input('Entre com o segundo coeficiente:\n'))
n3=int(input('Entre com o terceiro coeficiente:\n'))
delta=((n2**2)-(4*n1*n3))
x1=(-n2+(delta**0.5))/(2*n1)
x2=(-n2-(delta**0.5))/(2*n1)
if (n1==0):
    print('Error! Entre com um valor abaixo ou acima de 0')
else:
    print(f'Suas raízes são {x1:.2f} e {x2:.2f}')
    