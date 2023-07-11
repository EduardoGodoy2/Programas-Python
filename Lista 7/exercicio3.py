#Faça um programa que preencha por leitura um vetor de 5 posições, e informe a posição em que um valor x (lido do teclado) está no vetor. 
# Caso o valor x não seja encontrado, o programa deve imprimir o valor -1.  
# Faça a questão de duas formas: não utililizandoo método index() e utilizando o método index().
#lista=[]
#for i in range (5):
#    lista.append(float(input('Entre com uma posição:\n')))
#pos=float(input('Escolha um valor para achar sua posição:\n'))
#if (pos in lista):
#    print(f'Sua posição é {lista.index(pos)}')
#else:
#    print('-1')
lista=[]
for i in range (5):
    lista.append(float(input('Entre com uma posição:\n')))
pos=float(input('Escolha um valor para achar sua posição:\n'))
if (pos in lista):
    for i in range (5):
        if (lista[i]==pos):
            print(f'Sua posição é {i}')
else:
    print('-1')