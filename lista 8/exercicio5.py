#Faça um programa que leia a ordem de uma matriz quadrada A (até 100), 
# posteriormente leia seus valores e escreva sua transposta AT, onde AT[i][j] = A[j][i]
matriz1=[]
ordem=int(input('Entre com seu valor de ordem:\n'))
for i in range (ordem):
    linha=[]
    for j in range (ordem):
        linha.append(int(input(f'Entre com seu valor [{i}] e [{j}] da matriz:\n')))
    matriz1.append(linha)
matriz2=[]
for i in range (ordem):
    linha=[]
    for j in range (ordem):
        linha.append(matriz1[j][i])
    matriz2.append(linha)
for i in range (ordem):
    print(matriz1[i])
for i in range (ordem):
    print(matriz2[i])