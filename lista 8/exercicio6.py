#Uma pista de Kart permite 10 voltas para cada um de 6 corredores. 
# Faça um programa que leia os nomes e os tempos (em segundos) de cada volta de cada corredor e guarde as informações em uma matriz. 
# Ao final, o programa deve informar:
# a. De quem foi a melhor volta da prova, e em que volta
# b. Classificação final em ordem (1º o campeão)
# c. Qual foi a volta com a média mais rápida
matriz=[]
mtempo=0
volta=0
mtempon=0
round=0
for i in range(2):
    linha=[]
    nome=input(f'Digite o nome do corredor {i}:\n')
    linha.append(nome)
    for j in range(2):
        tvolta=float(input(f'Entre com o tempo do piloto {nome} na volta {j}:\n'))
        if (volta==0):
            mtempo=tvolta
            mtempon=nome
            round=j
            volta+=1
        linha.append(tvolta)
        if (tvolta<mtempo):
            mtempo=tvolta
            mtempon=nome
            round=j
    matriz.append(linha)
mediav=0
mmediav=0
vmr=0
for j in range(1,3):
    for i in range(2):
        mediav+=matriz[i][j]
    mediav/=2
    if (volta==0):
        mmediav=mediav
        vmr=j
        volta+=1
    if (mediav<mmediav):
        vmr=j
print(f"A melhor volta foi do(a) {mtempon}, na volta {round}, com o tempo {mtempo}.")
print(f"A volta com a média mais rápida foi a {vmr}.")