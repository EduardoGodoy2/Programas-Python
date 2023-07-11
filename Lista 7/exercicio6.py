#dado um vetor de 100 elementos, determine o maior e o menor elemento do vetor. (Utilize as funções min() e max() )
lista=[]
total_elementos=100
for i in range (total_elementos):
    lista.append(int(input('Entre com um elemento:\n')))
print(f'O menor valor da lista é {min(lista)} e o maior é {max(lista)}')