# Faça um programa que leia o nome do usuário e o imprima na vertical, em forma de escada, 
# usando apenas letras maiúsculas.
# Exemplo:Nome = Vanessa
# Resultado gerado pelo programa:
# V
# VA
# VAN
# VANE
# VANES
# VANESS
# VANESSA
nome=input('Entre com um nome:').upper()
for i in range(len(nome)):
    print(nome[:i+1:])