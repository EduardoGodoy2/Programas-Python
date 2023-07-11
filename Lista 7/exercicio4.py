#Um dado é lançado 50 vezes, e o valor correspondente é armazenado em um vetor. 
# Faça um programa que determine o percentual de ocorrências de face 6 do dado dentre esses 50 lançamentos. 
# Obs:  utilize a função randint() para gerar os 50 lançamentos do dados. randint(1,6) gera números inteiros aleatórios de 1 a 6.
# Insira no seu programa: fromrandomimportrandint
from random import randint
lista= []
for i in range (50):
    lista.append(randint(1,6))
oc=lista.count(6)
aux=lista.count(6)
oc=(oc*100)/50
print(f'Em 50 lançamentos o dado atingiu o 6 {aux} vezes e {oc}% das vezes.')