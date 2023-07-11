# Faça um programa que leia a altura e o sexo (codificado em 1=masculino e 2=feminino) de um grupo de n pessoas lidas do teclado. 
# Calcule e escreva:
# a) Média da altura dos grupos
# b) Média da altura dos homens
# c) Média da altura das mulheres
# d) Maior altura do grupo
# e) Menor altura do grupo
n=int(input('Digite quantas pessoas irão participar:\n'))
quanth=0
quantm=0
salturah=0
salturam=0
phomem=False
pmulher=False
for i in range(1,n+1):
    sexo=int(input('Digite qual seu sexo sendo 1=masculino e 2=feminino:\n'))
    if (sexo==1):
        alturah=float(input('Digite sua altura:\n'))
        salturah+=alturah
        quanth+=1
        if (phomem==False):
            menorh=alturah
            maiorh=alturah
            phomem=True
        else:
            if (alturah<menorh):
                menorh=alturah
            if (alturah>maiorh):
                maiorh=alturah
    else:
        alturam=float(input('Digite sua altura:\n'))
        salturam+=alturam
        quantm+=1
        if (pmulher==False):
            menorm=alturam
            maiorm=alturam
            pmulher=True
        elif (alturam<menorm):
            menorm=alturam
        elif (alturam>maiorm):
            maiorm=alturam
mgrupos=((salturah+salturam)/(quanth+quantm))
mediah=salturah/quanth
mediam=salturam/quantm
print(f'a média da altura dos grupos é {mgrupos}')
print(f'a média da altura dos homens é {mediah}')
print(f'a média da altura das mulheres é {mediam}')
print(f'a maior altura dos homens é {maiorh}')
print(f'a menor altura dos homens é {menorh}')
print(f'a maior altura das mulheres é {maiorm}')
print(f'a menor altura das mulheres é {menorm}')