# Faça um programa que leia um peso no planeta Terra e o número de um planeta e imprima o valor do seu peso neste planeta. 
# A relação dos planetas é dada a seguir juntamente com o valor das gravidades relativas ao planeta Terra.
from re import U


pesot=float(input('Entre com seu peso:\n'))
nplaneta=int(input('Entre com o número de um planeta 1-6:\n'))
if (nplaneta>=7) or (nplaneta<=0):
    print('Error! Número de planeta inválido.')
else:
    if (nplaneta==1):
        print(f'Seu peso em Mercúrio é {pesot*0.37}.')
    elif (nplaneta==2):
        print(f'Seu peso em Vênus é {pesot*0.88}.')
    elif (nplaneta==3):
        print(f'Seu peso Marte é {pesot*0.38}.')
    elif (nplaneta==4):
        print(f'Seu peso em Júpiter é {pesot*2.64}.')
    elif (nplaneta==5):
        print(f'Seu peso em Saturno é {pesot*1.15}.')
    else:
        print(f'Seu peso em Urano é {pesot*1.17}.')