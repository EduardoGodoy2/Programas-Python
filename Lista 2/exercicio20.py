# Faça um programa  que leia 3 números e diga se eles podem ou não tomar um triângulo.  
# Obs.: para formar um triângulo é necessário que a soma de dois lados seja sempre maior que o terceiro lado.
n1=int(input('Entre com um número:\n'))
n2=int(input('Entre com outro número:\n'))
n3=int(input('Entre com outro número:\n'))
maior=n1
if (maior<n2):
    maior=n2
if (maior<n3):
    maior=n3
elif (maior==n1):
    if (n2+n3>n1):
        print(f'{n2} + {n3} podem tomar o triângulo')
    else:
        print(f'{n2} + {n3} não podem tomar um triângulo')
elif (maior==n2):
    if (n1+n3):
        print(f'{n1} + {n3} podem tomar o triângulo')
    else:
        print(f'{n1} + {n3} não podem tomar o triângulo')
elif (maior==n3):
    if (n2+n1):
        print(f'{n2} + {n1} podem tomar o triângulo')
    else:
        print(f'{n2} + {n1} não podem tomar o triângulo')
