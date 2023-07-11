#Faça um programa que leia uma matriz 6x3 com números reais, calcule e mostre: 
# (a) o maior elemento da matriz e sua respectiva posição (linha e coluna); 
# (b) o menor elemento da matriz e sua respectiva posição.
matriz=[]
aux=0
aux2=0
aux3=0
aux4=0
maior=0
menor=0
l=4
c=4
for i in range(l):
    linha=[]
    for j in range(c):
        linha.append(int(input('Entre com um número:\n')))
    matriz.append(linha)
for i in range (l):
    for j in range(c):
        if (i==0) and (j==0):
            maior=matriz[i][j]
            aux=i
            aux2=j
        if (maior<matriz[i][j]):
            maior=matriz[i][j]
            aux=i
            aux2=j
for i in range(l):
    for j in range(c):
        if (i==0) and (j==0):
            menor=matriz[i][j]
            aux3=i
            aux4=j
        if (menor>matriz[i][j]):
            menor=matriz[i][j]
            aux3=i
            aux4=j
print(f'O maior elemento da matriz é {maior} e sua posição é {aux}{aux2} e o menor é {menor} e sua posição é {aux3}{aux4}')