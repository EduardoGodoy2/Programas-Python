#dado um vetor de 100 elementos, determine a diferença entre a soma dos elementos de índice par e a soma dos elementos de índice ímpar.
lista=[]
total_elementos=100
contpar=0
contimpar=0
dif=0
for i in range(total_elementos):
    lista.append(int(input('Entre com um valor:\n')))
for i in range(total_elementos):
    if (lista[i]%2==0):
        contpar+=lista[i]
    else:
        contimpar+=lista[i]
if (contpar>=contimpar):
    dif=contpar-contimpar
else:
    dif=contimpar-contpar
print(f'A diferença entre os elementos é de {dif} valores')