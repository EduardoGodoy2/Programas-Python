#Faça um programa que, dado uma figura geométrica que pode ser uma circunferência, triângulo ou retângulo, calcule a área e o perímetro da figura
# •O programa deve primeiro perguntar qual o tipo da figura:
# –(1) circunferência
# –(2) triângulo
# –(3) retângulo
# •Dependendo do tipo de figura, ler o (1) tamanho do raio da circunferência; (2) tamanho de cada um dos lados do triângulo; (3) tamanho dos dois lados retângulo
# •Usar funções sempre que possível
def per_circ(r):
    return 2*3.14*r
def area_circ(r):
    return 3.14*(r**2)
def per_triangulo(l1,l2,l3):
    return l1+l2+l3
def area_ret(b,h):
    return b*h
def per_ret(b,h):
    return 2*(b+h)


t=int(input('''
(1) circunferência
(2) triângulo
(3) retângulo
Escolha o tipo de figura de 1 a 3:'''))
if (t==1):
    r=int(input('qual o raio de sua circunferência:'))
    print(per_circ(r), area_circ(r))
if (t==2):
    l1=int(input('Entre com o primeiro lado do triângulo:'))
    l2=int(input('Entre com o segundo lado do triângulo:'))
    l3=int(input('Entre com o terceiro lado do triângulo:'))
    print(per_triangulo(l1,l2,l3))
if (t==3):
    b=int(int(input('Digite a base do seu retângulo:')))
    h=int(input('Digite a altura do seu retângulo:'))
    print(area_ret(b,h), per_ret(b,h))