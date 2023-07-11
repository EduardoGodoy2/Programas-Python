#dado um vetor de 100 elementos, determine o maior e o menor elemento do vetor. (Não utilize as funções min() e max() )
lista=[]
total_elementos=100
menor=0
maior=0
for i in range(total_elementos):
    lista.append(int(input('Entre com um valor:\n')))
for i in range(total_elementos):
    if (i==0):
        menor=lista[i]
        maior=lista[i]
    elif (lista[i]<=menor):
        menor=lista[i]
    elif (lista[i]>=maior):
        maior=lista[i]
print(f'O menor valor é {menor} e o maior número é {maior}')