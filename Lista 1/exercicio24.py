# Faça um programa que leia um valor inteiro representado uma certa quantidade em real (moeda), 
# e diga qual é o número máximo de notas de dois reais e o mínimo de moedas de um real em que esse valor pode ser representado.
valor=int(input('Entre com um valor:\n'))
moeda=valor%2
notas=valor//2
print(f'Esse valor tem {moeda} moedas e tem {notas} notas')