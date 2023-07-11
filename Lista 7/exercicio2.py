#Faça um programa que preencha por leitura um vetor de 10 posições, e conta quantos valores diferentes existem no vetor.
vet=[]
cont=0
for i in range(10):
    vet.append(int(input('valor')))
for i in range(10):
    for j in range(i+1,10):
        if (i+1!=j):
            cont+=1
print(cont)