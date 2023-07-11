# Faça uma função que receba um caractere retorne True se for consoante e False caso contrário
def tf(c):
    if (c in "bcdfghjklmnpqrstvwxyz"):
        return True
    else:
        return False

#Programa Principal
c=input('Entre com uma consoante:').lower()
print(tf(c))