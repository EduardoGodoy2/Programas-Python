#Faça um programa que leia uma matriz 3x3 de inteiros e retorne a linha de maior soma. Imprima na tela a matriz, a linha de maior soma e a soma. 
# Obs.: Em Python existe uma função sum() que efetua a soma dos elementos de uma lista. 
# Faça a questão de duas maneiras: utilizando e não utilizando a função sum().
matriz=[]
for i in range(3):
    linha=[]
    for j in range(3):
        linha.append(int(input(f'Entre com um valor na sua matriz [{i}][{j}]')))
    matriz.append(linha)
soma=0
maior=0
for i in range(3):
    somador=0
    for j in range(3):
        somador+=matriz[i][j]
    if (somador>soma):
        soma=somador
        maior=i
for i in range(3):
    print(matriz[i])
print()
print(matriz[maior])
print()
print(soma)