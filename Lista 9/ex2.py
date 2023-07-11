def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n -1) + fibonacci(n -2)
n=int(input('Entre com seu número fibonacci:\n'))
print(f'Seu número é {n} e seu fibonacci é {fibonacci(n-1)}')