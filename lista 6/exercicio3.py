#Faça um programa que recebe uma frase e substitui todas as ocorrências de espaço por “#”
frase=input('Entre com uma frase:').strip()
for i in frase:
    if (i==" "):
        i='#'
    print(i, end= '')