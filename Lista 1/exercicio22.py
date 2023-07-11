#Faça um programa para calcular o volume de uma lata de óleo, utilizando a fórmula volume=PIxR2xaltura. Seu programa deve ler o raio e a altura da lata.
from cmath import pi
import math
raio=float(input('digite o raio da lata:\n'))
altura=float(input('digite a altura da lata:\n'))
volume=(pi*(raio**2)*altura)
print(f'Seu volume é {volume:.4f}')
math.pi
