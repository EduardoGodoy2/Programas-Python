#Faça uma função que receba um número inteiro e retorne True se o número for par e False se o número for ímpar
def v(n):
    if (n%2==0):
        return True
    else:
        return False

#Programa Principal
n=int(input('Entre com um número:'))
print(f'Seu número {n} é {v(n)}')