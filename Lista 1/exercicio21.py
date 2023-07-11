# Faça um programa que leia a temperatura em graus centígrados e a converta para graus Fahrenheit. 
# A fórmula de conversão é F=(9.C+160)/5, onde F é a temperatura em Fahreinheite C é a temperatura em centígrados
g=float(input('Digite os graus celsius:\n'))
fahre=((9*g)+160)/5
print(f'{g} graus celsius são {fahre} fahrenheits ')