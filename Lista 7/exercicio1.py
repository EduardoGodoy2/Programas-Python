#Faça um programa que leia dois vetores de 3 posições,
# que representam forças sobre um ponto no espaço 3D, e escreva a força resultante. 
# Dica: força resultante é obtida pela soma dos valores das coordenadas correspondentes nos dois vetores: (x1 + x2), (y1+ y2), (z1 + z2)
vetora=[]
for i in range(3):
    vetora.append(float(input(f'Digite a posição {i} do vetor A:')))
vetorb=[]
for i in range(3):
    vetorb.append(float(input(f'Digite a posição {i} do vetor B:')))
vetorc=[]
for i in range(3):
    vetorc.append(vetora[i]+vetorb[i])
print(f'O valor resultante é {vetorc} ')