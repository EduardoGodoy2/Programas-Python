def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n-1)
n=int(input('Digite um número para o fatorial:\n'))
print(f'O fatorial de {n} é {fatorial(n)}')