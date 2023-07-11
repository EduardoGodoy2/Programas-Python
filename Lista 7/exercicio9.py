#dado um vetor com 20 elementos, gerar outro vetor que contenha somente números múltiplos de 3 encontrados no primeiro vetor.
vet1=[]
total_elementos=4
for i in range(total_elementos):
    vet1.append(int(input('Entre com um valor:\n')))
vet2=[]
for i in range(total_elementos):
    if (vet1[i]%3==0):
        vet2.append(vet1[i])
print(vet2)