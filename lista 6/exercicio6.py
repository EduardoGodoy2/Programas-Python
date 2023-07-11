#.Faça um programa que leia o nome do usuário e mostre o nome de trás para frente, utilizando somente letras maiúsculas.
# Exemplo:Nome = Vanessa
# Resultado gerado pelo programa:ASSENAV
nome=input('Entre com um nome:').upper().strip()
for i in nome:
    i=nome[::-1]
print(i, end='')