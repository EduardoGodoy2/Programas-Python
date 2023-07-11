#Existem 20 candidatos à presidência, com códigos que variam de 1 até 20. 
# Codificou-se 21 para votos brancos e 22 para votos nulos. 
# Cada voto vem em um cartão (contendo só um voto) e o último cartão vem com o número 0 (zero). 
# Faça um programa que auxilie a operação dos votos, imprimindo a quantidade de votos de cada candidato, o número de votos em branco, o número de votos nulos e o total de votantes.
#  Imprima também o(s) candidato(s) que venceram a eleição e o número de votos do(s) vencedor(es).
lista=[]
votantes=0
vencedor=0
maior=0
for i in range(1,23,1):
    lista.append(int(input('Selecione o número de seu voto (1-22):\n')))
    votantes+=1
for i in range(1,21,1):
    print(f'O caondidato {i} recebeu {lista.count(i)} votos')
for i in range (21,22,1):
    print(f'Branco foi votado {lista.count(i)} vezes')
for i in range (22,23,1):
    print(f'Nulo foi votado {lista.count(i)} vezes')
print(f'A eleição teve {votantes} votantes')
for i in (1,23,1):
    if (i==0):
        vencedor=lista[i]
    if (((lista[i]*100)/22)>vencedor):
        vencedor=lista[i]
print(f'O vencedor é {vencedor}')

