#Faça uma função que receba um caractere retorne True se for vogal e False caso contrário
def tf(c):
    if (c=='a') or (c=='e') or (c=='i') or (c=='o') or (c=='u'):
        return True
    else:
        return False

#Programa Principal
c=input('Entre com uma vogal:').lower()
print(tf(c))