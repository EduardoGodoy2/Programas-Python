# Faça um programa que leia 10 números e imprima a raiz quadrada de cada número.
for i in range(1,11,1):
    n=int(input('Entre com um número:'))
    r=n**0.5
    print(f'a raíz quadrada de {n} é {r}')