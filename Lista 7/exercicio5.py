#Faça um programa que leia um vetor vet de 20 números inteiros. 
# O programa deve gerar, a partir do vetor lido, um outro vetor pos que contenha apenas os valores inteiros positivos de vet. 
# A partir do vetor pos, deve ser gerado um outro vetor semdup que contenha apenas uma ocorrência de cada valor de pos.
vet=[]
num_inteiros=20      
for i in range(num_inteiros):
    vet.append(int(input('Entre com um valor inteiro:\n')))
pos=[]
for i in range(num_inteiros):
    if (vet[i]>0):
        pos.append(vet[i])
semdup=[]
for i in range(num_inteiros):
    check=pos[i] in semdup
    if (check==False):
        semdup.append(pos[i])
print(semdup)