#Faça um programa que leia dois números inteiros e imprima o dividendo, o divisor, o resto e o quociente.
dividendo=int(input('entre com o dividendo:\n'))
divisor=int(input('entre com o divisor:\n'))
resto=dividendo%divisor
quociente=dividendo/divisor
print(f'Seu dividendo é {dividendo}, seu divisor é {divisor}, seu resto é {resto} e seu quociente é {quociente}')