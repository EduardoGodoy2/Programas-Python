#Três massas m1, m2 e m3 estão separadas por distâncias r12, r13, r23, como mostra a figura.
m1=float(input('entre com o valor m1:\n'))
m2=float(input('entre com o valor m2:\n'))
m3=float(input('entre com o valor m3:\n'))
r12=float(input('entre com o valor r12:\n'))
r13=float(input('entre com o valor r13:\n'))
r23=float(input('entre com o valor r23:\n'))
g=6.67*(10**-11)
f= g*(((m1*m2)/(r12**2)) + ((m1*m3)/(r13**2)) + ((m2*m3)/(23**2)))
print(f'{f}')