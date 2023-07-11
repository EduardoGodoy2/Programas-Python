#Faça um programa que leia as dimensões de duas matrizes A e B, e depois leia as duas matrizes. 
# Se as matrizes forem de tamanhos compatíveis para multiplicação, multiplique as matrizes. 
# Imprima as matrizes A, B e a matriz resultante da multiplicação.
matriza=[]
la=int(input('Entre com o número de linhas da sua matriz A:\n'))
ca=int(input('Entre com o número de colunas da sua matriz A:\n'))
for i in range(la):
    linha=[]
    for j in range(ca):
        linha.append(int(input(f'Digite o elemento da sua posição [{i}][{j}]:\n')))
    matriza.append(linha)
matrizb=[]
lb=int(input('Entre com o número de linhas da sua matriz B:\n'))
cb=int(input('Entre com o número de colunas da sua matriz B:\n'))
for i in range(lb):
    linha=[]
    for j in range(cb):
        linha.append(int(input(f'Digite o elemento da sua posição [{i}][{j}]:\n')))
    matrizb.append(linha)
matrizs=[]
if (la==lb) and (ca==cb):
    for i in range(la):
        linha=[]
        for j in range(cb):
            linha.append(matriza[i][j]*matrizb[i][j])
        matrizs.append(linha)
    for i in range(la):
        print(matriza[i])
    print()
    for i in range(lb):
        print(matrizb[i])
    print()
    for i in range(la):
        print(matrizs[i])
else:
    print('Impossivel multiplicar.')