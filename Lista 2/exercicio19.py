# Faça um programa que leia 3 nomes e os coloque em ordem alfabética.
nome1=input('Digite um nome:\n').lower()
nome2=input('Digite outro nome:\n').lower()
nome3=input('Digite outro nome:\n').lower()
if (nome1==nome2) or (nome1==nome3) or (nome3==nome2):
    print('Error!')
elif (nome1<nome2) and (nome2<nome3):
    print(f'{nome1}, {nome2}, {nome3}')
elif (nome1>nome2) and (nome2>nome3):
    print(f'{nome3}, {nome2}, {nome1}')
elif (nome1<nome2) and (nome1>nome3):
    print(f'{nome3}, {nome1}, {nome2}')
elif (nome1<nome3) and (nome2>nome3):
    print(f'{nome1}, {nome3}, {nome2}')
elif (nome1>nome3) and (nome3>nome2):
    print(f'{nome2}, {nome3}, {nome1}')
else:
    print(f'{nome3}, {nome1}, {nome2}')