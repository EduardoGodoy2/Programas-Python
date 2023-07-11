#Faça um programa que leia duas matrizes A e B 2x2 e imprima a matriz C que é a soma das matrizes A e B.
matriza=[]
matrizb=[]
matrizc=[[0,0],[0,0]]
for i in range(2):
    linha= []
    for j in range(2):
        linha.append(int(input('Entre com o valor da sua matriz A:\n')))
    matriza.append(linha)
for i in range(2):
    linha = []
    for j in range(2):
        linha.append(int(input('Entre com o valor de sua matriz B:\n')))
    matrizb.append(linha)
for i in range(2):
    for j in range(2):
        matrizc[i][j]=matriza[i][j]+matrizb[i][j]
for i in range(2):
    print(matrizc[i])