#Faça um programa que leia o raio de uma circunferência e calcule o perímetro e a área da circunferência.
from cmath import pi
import math


raio=int(input('Digite o raio da circunferência:\n'))
c=2*pi*raio
a=pi*(raio**2)
print(f'O perímetro da circunferência é {c:.2f}, e a área é {a:.2f}')
math.pi