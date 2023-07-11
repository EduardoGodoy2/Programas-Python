#Faça uma função que retorne o valor absoluto de um número
def vabsoluto(v):
    if (v >= 0):
        return v
    else:
        return v - 2 * v

#Programa Principal
v=int(input("Entre com um valor:"))
print(f'O valor absoluto do seu número é {vabsoluto(v)} ')