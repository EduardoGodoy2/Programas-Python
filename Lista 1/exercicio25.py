#Faça um programa que leia o valor gasto com as despesas em um restaurante e imprima o valor da conta com uma gorjeta de 10%.
g=float(input('Digite seu gasto no restaurante:\n'))
gorjeta=g*0.1
valortotal=gorjeta+g
print(f'Seu valor gasto mais a gorjeta é {valortotal}')